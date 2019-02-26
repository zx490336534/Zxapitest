#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:zhongxin
# datetime:2019/2/25 11:09 PM
from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('forgot/', views.ForgotView.as_view(), name='forgot'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('reset/', views.ResetView.as_view(), name='reset'),
]
