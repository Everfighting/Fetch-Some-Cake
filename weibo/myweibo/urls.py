from django.contrib import admin
from django.urls import path, include

from myweibo.views import get_user_info
app_name='myweibo'
urlpatterns = [

    path('weibologin/',get_user_info,name='get_user_info')
]