from django.shortcuts import render
from django.http import HttpResponse


def taskList(request):
    return render(request , 'index.html')

def details(request):
    return render(request,'detail.html')