"""Attendance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import main.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('detail/<int:name_id>',main.views.detail,name="detail"),
    path('',main.views.main,name="main"),
    path('chk',main.views.chk,name="chk"),
    path('date',main.views.date,name="date"),
    path('show',main.views.show,name="show"),
    path('show1',main.views.show1,name="show1"),
    path('member',main.views.member,name="member"),
    path('member_add',main.views.member_add,name="member_add"),
    path('member_add1',main.views.member_add1,name="member_add1"),
]
