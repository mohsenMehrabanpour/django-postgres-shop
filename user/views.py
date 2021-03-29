from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from mohsen_tools.validator import signup_validator
from user.models import User
from django.db import transaction
from django.contrib import messages


class login(View):

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, 'login.html')
        messages.warning(request, 'you already logged in')
        return render(request, '404.html')

    def post(self, request):
        if request.user.is_authenticated:
            return Http404
        user = authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            django_login(request, user)
            return HttpResponse('login successfully')
        else:
            messages.error(request, 'your username or password is wrong')
            return redirect(reverse('login_page'))


class signup(View):

    def get(self, request):
        if request.user.is_authenticated:
            messages.error('you already created your account')
            return render(request, '404.html')
        return render(request, 'signup.html')

    def post(self, request):
        result = signup_validator(request.POST)
        if result == 'ok':
            try:
                with transaction.atomic():
                    user = User.objects.create_user(
                        username=request.POST['username'], password=request.POST['password'])
                    user.first_name = request.POST['firstname']
                    user.last_name = request.POST['lastname']
                    user.phone_number = request.POST['phonenumber']
                    user.address = request.POST['address']
                    user.email = request.POST['email']
                    user.save()
                    messages.success(
                        request, 'your account created successfully')
                    return redirect(reverse('login_page'))
            except:
                messages.error(
                    request, 'there was some problem during create your account, please try again')
                return redirect(reverse('signup_page'))
        else:
            for message in result:
                messages.error(request,message)
            return redirect(reverse('signup_page'))
