
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from adminapp.models import adminUploadvideos, categoryDetails
from adminapp.serialisers import adminupload_serialiser, categoryDetails_serialiser

# Create your views here.

class categoryview(APIView):

    def get(self, request, format=None):
        snippets = categoryDetails.objects.all()
        serializer = categoryDetails_serialiser(snippets, many=True)
        return Response( {"status":status.HTTP_200_OK,"Message":"Reterived Successfully","data":serializer.data})

    def post(self, request, format=None):
      
        serializer =categoryDetails_serialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":status.HTTP_200_OK,"Message":"Updated Successfully","data":serializer.data})
        # return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class adminUploadview(APIView):

    def get(self, request, format=None):
        snippets = adminUploadvideos.objects.all()
        serializer = adminupload_serialiser(snippets, many=True)
        return Response( {"status":status.HTTP_200_OK,"Message":"Reterived Successfully","data":serializer.data})

    def post(self, request, format=None):
      
        serializer =adminupload_serialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":status.HTTP_200_OK,"Message":"Updated Successfully","data":serializer.data})
        # return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

