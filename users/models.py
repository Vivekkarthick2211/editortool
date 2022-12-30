from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from editorTool import settings
def uservideouploadpath(instance,filename):
     return os.path.join('documents','userid', filename)
# Create your models here.
class myUser(AbstractUser):
  phone_no = models.CharField(max_length = 10)

class UserHistory(models.Model):
    UserID=models.ForeignKey( settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    Video=models.FileField(blank=False,upload_to=uservideouploadpath)	
    Category=models.CharField(max_length=50,null=False,blank=False)
    ChooseDate=models.DateTimeField(auto_now_add=True)
    VideoTitle=models.TextField()
    sumprice=models.FloatField(blank=False,null=False)

