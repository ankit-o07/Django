
from django.contrib import admin
from django.urls import path , include
from .views import  signup ,login_user ,home , logout_user

urlpatterns = [
    path("", signup,name="signup"),
    path("login/",login_user,name="login"),
    path('home/', home,name="home"),
    path('logout/', logout_user, name="Logout")
]