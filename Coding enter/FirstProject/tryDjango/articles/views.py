from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, logout, login
from random import randint
from articles.models import Article
from .froms import ArticlesForm
# Create your views here.


@login_required
def article_create_view(request):

    context = {
        "from": ArticlesForm()
    }
    if not request.user.is_authenticated:
        return redirect("/login")
    if request.method =="POST":
        form = ArticlesForm(request.POST)
        if form.is_valid():

            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            Article.objects.create(title=title, content=content)
    
    return render(request,"articles/create.html",context=context)


def article_search_view(request):
    query_dict = request.GET   # this is dictionary
    
    try:
        query = int(query_dict.get("q"))
    except:
        query = None

    if query is not None:
        article_obj = Article.objects.get(id=query)

    context  ={
        "object": article_obj
    }
    return render(request,"articles/search.html",context=context)

def article_detail_view(request,id=None):
    article_obj = None
    if id is not None:

        article_obj = Article.objects.get(id=id)
        article_queryset = Article.objects.all()

    context ={
        "object_list" : article_queryset,
        "object" : article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }
    return render(request, "articles/detail.html", context)
