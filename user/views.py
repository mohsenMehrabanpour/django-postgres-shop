from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from mohsen_tools.context_message import create_message

class login(View):

    def get(self,request):
        if not request.user.is_authenticated:
            return render(request,'login.html')
        messages = create_message('error','you alrady logged in')
        return render(request,'404.html',messages)

    def post(self,request):
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            self.logged_in = True
            django_login(request,user)
            return HttpResponse('login successfully')
        else:
            messages = create_message('error','your username or password is wrong')
            return render(request,'login.html',messages)


class signup(View):
    
    def get(self,request):
        if request.user.is_authenticated:
            message = create_message('error','you create your account already')
            return render(request,'404.html',message)
        return render(request,'signup.html')