from django.contrib.auth.models import User

from users.models import UserHistory, myUser
from users.serialisers import UserHistorySerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.views.generic import View
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
# Create your views here.
class Regview(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = myUser.objects.all()
        serializer = UserSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        dictnew={}
        for key,val in request.data.items():
            if key=='password':
                dictnew.update({key:make_password(val)})  
            else:
                dictnew.update({key:val})    
        serializer =UserSerializer(data=dictnew)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(APIView):
    def post(self, request):
        usename = request.POST['username']
        pasword = request.POST['password']
        user = authenticate(username=usename, password=pasword)
        if user is  not None:
            snippets = User.objects.filter(username=usename)
    
            serializer = UserSerializer(snippets, many=True)
            
            if user.is_active:
                # login(request, user)
                return Response({"status":status.HTTP_200_OK,"message":"login successfull","data":serializer.data})
            else:
                return Response({"status":status.HTTP_200_OK,"message":"login successfull","data":serializer.data})
        else:
            # pass
            return Response({"status":status.HTTP_400_BAD_REQUEST,"message":"login not successfull","data":[]})


class userHistoryview(APIView):

    def get(self, request, format=None):
        snippets = UserHistory.objects.all()
        serializer = UserHistorySerializer(snippets, many=True)
        return Response( {"status":status.HTTP_200_OK,"Message":"Reterived Successfully","data":serializer.data})

    def post(self, request, format=None):
      
        serializer =UserHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":status.HTTP_200_OK,"Message":"Updated Successfully","data":serializer.data})
        # return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
