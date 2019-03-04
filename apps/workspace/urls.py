#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:zhongxin
# datetime:2019/3/4 10:16 PM
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
]
