from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.taskList,name='tasks'),
    path('details/', views.details,name="detail")
]