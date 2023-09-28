from django.contrib import admin
from django.urls import path, include
from .views import home , create
urlpatterns = [
    path('',home,name="Home"),
    path('create/', create, name="create"),
]