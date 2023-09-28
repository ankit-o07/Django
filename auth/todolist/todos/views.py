from django.shortcuts import render , redirect
from .models import Todo


# Create your views here.

def home(request):
    obj = Todo.objects.all()
    params = {
        "object" : obj,
        "range" : (0,len(obj)-1)
        
    }
        
    # print(params)
    return render(request,"basic.html",params)


def create(request):
    
    if request.method == 'POST':
        
        title = request.POST.get('title', '')
        detail = request.POST.get('detail', '')
        todo = Todo.objects.create(title=title, discription=detail)
        todo.save()
        return redirect("/")
    return render(request, 'create.html')

def update(request):
    if request.method == 'POST':

        title = request.POST.get('title', '')
        detail = request.POST.get('detail', '')

        obj = Todo.objects.values('title','')
        
        
        return redirect("/")
    

    return render(request, "update.html")



# def login_user(request):
#     if request.method == "POST":
#         form = 