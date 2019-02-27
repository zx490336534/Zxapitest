#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:zhongxin
# datetime:2018/12/18 10:52 PM

from django.db import models


class ModelBase(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        # 为抽象模型类，用于其他模型来继承，数据库迁移时不会创建ModelBase表
        abstract = True
