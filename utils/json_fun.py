#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:zhongxin
# datetime:2018/12/7 9:36 PM
from django.http import JsonResponse

from .res_code import Code


def to_json_data(errno=Code.OK, errmsg='', data=None, **kwargs):
    json_dict = {'errno': errno, 'errmsg': errmsg, 'data': data}

    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        json_dict.update(kwargs)

    return JsonResponse(json_dict)
