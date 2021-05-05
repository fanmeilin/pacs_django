"""service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse
from server import  views  as server_views

urlpatterns = [
    path('',server_views.index),
    path('admin/', admin.site.urls),
    path('index/',server_views.index),
    path('dcmViewer/',server_views.dcmViewer),
    path('upload/',server_views.upload),
    path('login/',server_views.login),
    path('logout/',server_views.logout),
    path('register/',server_views.register),
    path('dcmTemp/',server_views.dcmTemp),
    path(r'read/',server_views.read),
    path('read0/',server_views.read0),
    path('read1/',server_views.read1),
    path('read2/', server_views.read2),
    path('read3/', server_views.read3),
    path('read4/', server_views.read4),
    path('read5/', server_views.read5),
    path('read6/', server_views.read6),
    path('read7/', server_views.read7),
    path('read8/', server_views.read8),
    path('read9/', server_views.read9),
]
