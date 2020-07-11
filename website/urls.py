from django.contrib import admin
from django.urls import path
from website.views import index,login2
from rest_framework.urlpatterns import format_suffix_patterns
from website.views import list

urlpatterns = [

    path('index',index,name='index'),
    path('login',login2,name='login2'),
    path('list',list.as_view())

]

