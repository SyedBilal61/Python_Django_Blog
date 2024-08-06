"""
URL configuration for Event_management_proj project.

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
from django.urls import path, include
from .import views

urlpatterns = [
     # Login page Views here 

    path ('',views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),

    path('index/',views.index , name='index'),
    path('all_evn/',views.all_evn , name='all_evn'),  
    path('add_evn/',views.add_evn , name='add_evn'),
    path('remove_evn/',views.remove_evn , name='remove_evn'),
    path('remove_evn/<int:evn_id>',views.remove_evn , name='remove_evn'),
    path('filter_evn/',views.filter_evn, name='filter_evn'),
    path('logout/',views.LogoutPage,name='logout')]
