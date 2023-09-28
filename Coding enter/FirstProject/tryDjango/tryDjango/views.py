'''
To render html web pages
'''
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article
from django.shortcuts import render
from random import randint



def home_view(request,id = None):
    '''
    Take in a request(Django send request )
    Return HTML as a response(We pick to return the response)
    '''
    
    # from datbase ??
    id = randint(1,5)
    article_obj = Article.objects.get(id=id)
    my_list = [102,13,345,1331,213]

    article_queryset = Article.objects.all()
    
    

    context ={
        "object_list" : article_queryset,
        "object" : article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content
    }
    print(context)
    #HTML_STRING = render_to_string("home_view.html", context=context)
    #return HttpResponse(HTML_STRING)

    return render(request, "home_view.html",context)


