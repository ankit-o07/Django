from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    params ={
        "name":"ankit"
    }
    ans ={
        "ans":"36"
    }

    return render(request,"index.html",ans)


def index(request):
    return HttpResponse("<h1>I am index</h1>")