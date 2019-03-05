from django.shortcuts import render
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'index/index.html')


class CallectionsView(View):
    def get(self, request):
        return render(request, 'index/callections.html')
