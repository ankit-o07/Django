from django.contrib import admin
from django.urls import path , include
from .views import test , login_view, logout_view ,signup_view

urlpatterns = [
    
    path("",test,name="Test"),
    path("login/",login_view, name="Login"),
    path("logout/",logout_view, name="Logout"),
    path("signup/",signup_view, name="Signup"),


]
