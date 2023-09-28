from django.shortcuts import render
from django.http import HttpResponse
from .forms import myForm
# Create your views here.


def form(request):
    fn = myForm()
    data = {
        'form':fn
    }

    if request.method == "POST":
        if fn.is_valid:
            num1 = int(request.POST.get("num1",""))
            num2 = int(request.POST.get("num2",""))
            fin = num1 + num2
            data = {
                'form' : fn,
                "fin" : fin

            }
            return render(request , 'index.html',data)

    return render(request , 'index.html',data)