from django.urls import path
from .views import login_user, register_user

urlpatterns = [
    path('user/login/', login_user, name="user-login"),
    path('user/register/', register_user, name="user-register")
]