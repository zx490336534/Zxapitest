from django.shortcuts import render
from django.views import View


class LoginView(View):
    def get(self, request):
        return render(request, 'login/index.html')


class ForgotView(View):
    def get(self, request):
        return render(request, 'login/forgot.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'login/register.html')


class ResetView(View):
    def get(self, request):
        return render(request, 'login/reset.html')
