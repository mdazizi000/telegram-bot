from django.urls import path
from .views import register, login_account,  user_profile , user_profile_additional ,logout_account

urlpatterns = [
    path("register" , register),
    path("login" , login_account),
    path("logout" , logout_account),
    path("profile" , user_profile),
    path("profile_additional" , user_profile_additional),


]