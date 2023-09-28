from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import  UserCreationForm ,AuthenticationForm
from .add_Todo import TodoForm
from .models import Todo
# Create your views here.

@login_required(login_url="login")
def home(request):
    if request.user.is_authenticated:
        user = request.user
        todos = Todo.objects.filter(user =user).order_by("priority")
        
        params = {
            "title" : "Home",
            "todo" : todos,
        }
        return render(request , "index.html" , params)

    



def sigup_view(request):
    params = {
        "title" : "Signup"
        }
        
    if request.method == "POST":
        
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        email = request.POST.get("email","")
        

        my_user = User.objects.create_user(username=username,email=email,password=password)
        
        my_user.save()
        
        
        return redirect("login")
    return render(request , "signup.html" , params)


def login_view(request):

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username= username , password= password)
        print(user)
        print("test1")
        if user is not None :
            print("test2")
            login(request, user)
            return redirect("Home")
        else :
            print("test3")
            return redirect("login")  
      
    params = {
        "title" : "Login"
    }
    return render(request, "login.html" ,params )

       
        


def logout_view(request):
    logout(request)

    params = {
        "title" : "login"
    }
    return render(request, "login.html")
    

def addTodo(request):
    if request.user.is_authenticated:
        user = request.user
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()

            return redirect("Home")
        else :
            params = {
                "form" : form
            }
            return render(request,'addTodo.html',params)
def delete(request ,id):
    Todo.objects.get(pk = id).delete()
    return redirect("Home")

def status(request,id ,st):
    todo = Todo.objects.get(pk = id)
    todo.status = st
    todo.save()
    return redirect("Home")
def update(request,id):
    pass