from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from adminapp.views import adminUploadview, categoryview

urlpatterns = [
   path('categoryinsert/',categoryview.as_view()),
   path('adminuploadview/',adminUploadview.as_view())
]