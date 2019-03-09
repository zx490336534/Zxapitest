#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:zhongxin
# datetime:2019/3/4 10:16 PM
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('callections/', views.CallectionsView.as_view(), name='callections'),
    path('callections/<int:callections_id>/', views.CallectionsEditView.as_view(), name='callections_edit'),
    path('apiadd/', views.ApiAddView.as_view(), name='api_add'),
]
