from django.urls.conf import re_path
from user.views import login, signup, Dashboard, Notfount
from django.urls import path

urlpatterns = [
    path('login/', login.as_view(), name='login_page'),
    path('signup/', signup.as_view(), name='signup_page'),
    path('dashboard/', Dashboard.as_view(), name='dashboard_page'),
    re_path(r'^\w*\W*\d*\D*\s*\S*/$', Notfount.as_view(), name='notfound_page')
]
