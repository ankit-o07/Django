from django.shortcuts import render  ,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login ,logout
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url="login")
def home(request):
    return render(request , 'home.html')

def signup(request):
    if request.method == "POST":
        
        uname = request.POST.get("username","")
        email = request.POST.get("email", "")
        pass1 = request.POST.get("password1","")
        # pass2 = request.POST.get("password2","") 
        my_user = User.objects.create_user(uname,email,pass1)
        my_user.save()
        return redirect("/login")
             
    return render(request, 'signup.html')



def login_user(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pass1 = request.POST.get("pass")
        user = authenticate(request ,username=uname ,password=pass1)
        if user is not None :
            login(request,user)
            return redirect("/home")
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect("/login")
