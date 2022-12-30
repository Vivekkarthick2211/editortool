from adminapp.models import adminUploadvideos, categoryDetails
from rest_framework import serializers

class categoryDetails_serialiser(serializers.ModelSerializer):
   class Meta:
       model = categoryDetails
       fields = "__all__"
class adminupload_serialiser(serializers.ModelSerializer):
   class Meta:
       model = adminUploadvideos
       fields = "__all__"