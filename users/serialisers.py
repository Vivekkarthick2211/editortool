from rest_framework import serializers
from users.models import   UserHistory, myUser
class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = myUser
       fields = "__all__"

class UserHistorySerializer(serializers.ModelSerializer):
    class Meta:
       model = UserHistory
       fields = "__all__"
