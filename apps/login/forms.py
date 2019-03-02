#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:zhongxin
# datetime:2019/2/28 10:43 PM
import re
from django import forms
from .models import User
import re
from django import forms
from django.db.models import Q
from django.contrib.auth import login, logout
from login import constants


class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=20, min_length=5,
                               error_messages={"min_length": "用户名长度要大于5", "max_length": "用户名长度要小于20",
                                               "required": "用户名不能为空"}
                               )
    password = forms.CharField(label='密码', max_length=20, min_length=6,
                               error_messages={"min_length": "密码长度要大于6", "max_length": "密码长度要小于20",
                                               "required": "密码不能为空"}
                               )
    password_repeat = forms.CharField(label='确认密码', max_length=20, min_length=6,
                                      error_messages={"min_length": "密码长度要大于6", "max_length": "密码长度要小于20",
                                                      "required": "密码不能为空"}
                                      )
    email = forms.EmailField(required=True,
                             error_messages={'required': "邮箱不能为空"})

    def clean(self):
        cleaned_data = super().clean()
        passwd = cleaned_data.get('password')
        passwd_repeat = cleaned_data.get('password_repeat')

        if passwd != passwd_repeat:
            raise forms.ValidationError("两次密码不一致")


class LoginForm(forms.Form):
    """
    login form data
    """
    email = forms.EmailField()
    password = forms.CharField(label='密码', max_length=20, min_length=6,
                               error_messages={"min_length": "密码长度要大于6", "max_length": "密码长度要小于20",
                                               "required": "密码不能为空"}
                               )
    remember = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """
        self.request = kwargs.pop('request', None)
        super(LoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        """

        :return:
        """
        # 1.获取清洗之后的参数
        cleanded_data = super().clean()
        user_info = cleanded_data.get('email')
        passwd = cleanded_data.get('password')
        hold_login = cleanded_data.get('remember')
        # 2.查询数据库，判断用户账号和密码是否正确
        user_queryset = User.objects.filter(Q(email=user_info))
        if user_queryset:
            if user_queryset.get(password=passwd):
                # 3.是否将用户信息设置到会话中
                if hold_login:
                    self.request.session.set_expiry(constants.USER_SESSION_EXPIRES)
                else:
                    self.request.session.set_expiry(0)  # 关闭浏览器清空
            else:
                raise forms.ValidationError('用户密码有误，请重新输入！')
        else:
            raise forms.ValidationError('用户账号不存在，请重新输入！')
