"""
URL configuration for project29 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert_topic/',insert_topic,name='insert_topic'),
    path('display_topic/',display_topic,name='display_topic'),
    path('insert_webpages/',insert_webpages,name='insert_webpages'),
    path('display_webpages/',display_webpages,name='display_webpages'),
    path('insert_accessrecords/',insert_accessrecords,name='insert_accessrecords'),
    path('display_accessrecords/',display_accessrecords,name='display_accessrecords'),
    path('select_multiple_webpage/',select_multiple_webpage,name='select_multiple_webpage'),
    path('checkbox/',checkbox,name='chechbox'),
]
