#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Author:zhongxin 
#datetime:2019/2/25 11:09 PM 
from django.urls import path
from . import views

app_name = 'login'

urlpatterns = [
    path('',views.index)
]