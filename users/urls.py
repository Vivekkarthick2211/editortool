
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from users.video_editing import processingvideo

from users.views import LoginView, Regview, userHistoryview
urlpatterns = [
   path('register/',Regview.as_view()),
   path('LoginView/',LoginView.as_view()),
   path('userHistoryview/',userHistoryview.as_view()),
   path('processingapi/',processingvideo.as_view())
]