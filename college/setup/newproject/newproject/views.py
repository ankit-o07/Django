from django.shortcuts import HttpResponse

def index(response):
    return HttpResponse("Welcome to")