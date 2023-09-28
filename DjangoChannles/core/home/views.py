from django.shortcuts import render
from django.http import HttpResponse
import os
# Create your views here.
def home(request):
    a = ""
    if os.environ.get('SERVER_GATEWAY_INTERFACE') == 'Web':
        a = "wsgi"
    else:
        a = "asgi"
    return HttpResponse("<h1>"+ a+"</h1>")    