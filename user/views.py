from product.models import Product, Image, Category
from django.http.response import Http404
from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.views import View
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from mohsen_tools.validator import product_image_validator, signup_validator, product_text_validator
from user.models import User, Admin
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
            messages.success(request, 'welcome to your account')
            return redirect(reverse('dashboard_page'))
        else:
            messages.error(request, 'your username or password is wrong')
            return redirect(reverse('login_page'))


class signup(View):
    def get(self, request):
        if request.user.is_authenticated:
            messages.error(request, 'you already created your account')
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
                messages.error(request, message)
            return redirect(reverse('signup_page'))


class Dashboard(View):
    is_admin = False
    need_check = True

    def get(self, request):
        if not request.user.is_authenticated:
            messages.error(request, 'please login the system at first.')
            return redirect(reverse('login_page'))
        if self.need_check:
            self.is_admin = Admin.objects.filter(
                username=request.user).exists()
            self.need_check = False
        if self.is_admin:
            return render(request, 'admin_panel.html')
        return render(request, 'user_panel.html')

    def post(self, request):
        if self.need_check:
            self.is_admin = Admin.objects.filter(
                username=request.user).exists()
            self.need_check = False
        if self.is_admin:
            res = self.__admin_request_handler(request)
            if res == False:
                messages.error(
                    request, 'there is some problem during import product')
                return redirect(reverse('dashboard_page'))
            messages.success(request, 'product inserted successfully')
            return redirect(reverse('dashboard_page'))

    def __admin_request_handler(self, request):
        res = product_text_validator(request.POST)
        if res == False:
            return False

        img = request.FILES.get('image_file', None)
        cat = request.POST['category']
        
        if cat is not None:
            category = Category.objects.get_or_create(
                title=cat, defaults={'title': cat})
        if img is not None:
            if product_image_validator(img):
                image_model = Image()
                try:
                    with transaction.atomic():
                        product = Product.objects.create(**res)
                        image_model.image = img
                        image_model.product = product
                        product.category.add(category[0])
                        image_model.save()
                    return True
                except:
                    return False
            return False
        product = Product.objects.create(**res)
        return True


class Notfount(View):
    def get(self, request):
        messages.error(request, 'this page was not found')
        return render(request, '404.html')
