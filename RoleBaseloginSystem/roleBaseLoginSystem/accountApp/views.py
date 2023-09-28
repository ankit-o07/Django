from django.shortcuts import render ,redirect
from django.http import HttpResponse
from .forms import ProfileForm


# Create your views here.

def test(request):
    return render(request,"accountAppTemp/login.html")

def signup_view(request):
    profile_form =ProfileForm()
    data = {
        'form':profile_form
    }
    if request.method == "POST":
            name = request.POST.get("name","")
            print(name)
            return redirect("/account/login")
            
    
    return render(request,"accountAppTemp/signup.html", data)

def login_view(request):
    return render(request,"accountAppTemp/login.html")

def logout_view(request):
    return HttpResponse("<h1>you log out<h1>")


