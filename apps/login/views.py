import json
import logging
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth import login, logout
from login.forms import RegisterForm, LoginForm
from login.models import User
from utils.json_fun import to_json_data
from utils.res_code import Code, error_map
from . import models

logger = logging.getLogger('django')


class LoginView(View):
    def get(self, request):
        return render(request, 'login/index.html')

    def post(self, request):
        try:
            json_data = request.POST
            if not json_data:
                return to_json_data(errno=Code.PARAMERR, errmsg="参数为空，请重新输入")
            use_key = ["email", "password", "remember"]
            dict_data = {}
            for i in use_key:
                dict_data[i] = request.POST.get(i)
        except Exception as e:
            logging.info('错误信息:\n{}'.format(e))
            return to_json_data(errno=Code.UNKOWNERR, errmsg=error_map[Code.UNKOWNERR])
        form = LoginForm(data=dict_data, request=request)
        if form.is_valid():
            return redirect(reverse("index"))
        else:
            err_msg_list = []
            for item in form.errors.get_json_data().values():
                err_msg_list.append(item[0].get('message'))
            err_msg_str = '/'.join(err_msg_list)
            return to_json_data(errno=Code.PARAMERR, errmsg=err_msg_str)


class ForgotView(View):
    def get(self, request):
        return render(request, 'login/forgot.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'login/register.html')

    def post(self, request):
        json_data = request.POST
        if not json_data:
            return to_json_data(errno=Code.PARAMERR, errmsg="参数为空，请重新输入")
        if not request.POST.get('aggree'):
            return to_json_data(errno=Code.AGGREE, errmsg=error_map[Code.AGGREE])
        use_key = ['username', "password", "password_repeat", "email"]
        dict_data = {}
        for i in use_key:
            dict_data[i] = request.POST.get(i)
        form = RegisterForm(data=dict_data)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            user = User.objects.create(username=username, password=password, email=email)
            user.save()
            return render(request, 'login/index.html')
        else:
            # 定义一个错误信息列表
            err_msg_list = []
            for item in form.errors.get_json_data().values():
                err_msg_list.append(item[0].get('message'))
            err_msg_str = '/'.join(err_msg_list)
            return to_json_data(errno=Code.PARAMERR, errmsg=err_msg_str)


class ResetView(View):
    def get(self, request):
        return render(request, 'login/reset.html')
