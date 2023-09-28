from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def myapp(request):
    return HttpResponse("<h1 style='font-size:100px;'>MY APP<h1>")