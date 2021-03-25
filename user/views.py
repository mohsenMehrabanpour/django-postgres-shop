from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login

class login(View):

    def get(self,request):
        if not request.user.is_authenticated:
            return render(request,'login.html')
        return HttpResponse('already logged in')

    def post(self,request):
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            self.logged_in = True
            django_login(request,user)
            return HttpResponse('login successfully')
        else:
            return HttpResponse('something is wrong')
