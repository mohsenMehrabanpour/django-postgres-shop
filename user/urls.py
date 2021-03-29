from user.views import login, signup
from django.urls import path

urlpatterns = [
    path('login/', login.as_view(), name='login_page'),
    path('signup/', signup.as_view(), name='signup_page'),
]
