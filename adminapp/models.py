from django.db import models

from editorTool import settings
import os
def adminuploadpath(instance, filename):
    return os.path.join('documents','catgoryvideos', filename)
# def adminuploadpath():

# Create your models here.

class categoryDetails(models.Model):
    CategoryName=models.CharField(max_length=50,null=False,blank=False)
    adminId = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    CreatedDate=models.DateTimeField(auto_now_add=True)
    InfoOfCategory=models.TextField()

class adminUploadvideos(models.Model):
    VideoTemplate=models.FileField(blank=False,upload_to=adminuploadpath)
    CatId=models.ForeignKey(categoryDetails,on_delete=models.CASCADE)
    AdminId=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    VideoDetails=models.TextField(blank=True)
    VideoPrice=models.FloatField(blank=False,null=False)
    offer=models.FloatField(blank=False,null=False)
    Discount=models.FloatField(blank=False,null=False)	
    Activitystatus=models.CharField(max_length=20,blank=False,null=False) 
    uploaddate=models.DateTimeField(auto_now_add=True)
