from user.views import login
from django.urls import path

urlpatterns = [
    path('login/', login.as_view())
]
