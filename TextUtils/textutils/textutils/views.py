# I have created this File  ---Ankit
from django.http import HttpResponse
from django.shortcuts import redirect, render

def index(request):
    params = {'name':'Ankit','place':'Mars'}
    return render(request, 'index.html',params)
    #return HttpResponse("<h1>hello</h1>")


def analyze(request):
    #Get the text
    djtext = request.GET.get('text',"default")
    removepunc = request.GET.get('removepunc',"off")
    fullcaps   = request.GET.get('fullcaps',"off")
    newlineremover = request.GET.get('newlineremover','off')
    spaceremover   = request.GET.get("spaceremover" , 'off')
    charcount    = request.GET.get("charcount","off")
    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    
    
    
    #Analze the text
    if removepunc == "on":
        analyzed = ""
        for char in  djtext:
            if char not in punctuations:
                analyzed += char 
        
        params = {'purpose':'Remove Puntuations', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params )
    elif fullcaps == "on":
        analyzed = djtext
        analyzed = analyzed.upper()
        params = {'purpose':'fullcaps', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params )
    
    elif newlineremover == "on":
        analyzed = ""
        for char in  djtext: 
            if char !=  "\n":
                analyzed += char 
        
        params = {'purpose':'New line remover', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params )
    elif spaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if index != len(djtext)-1:
                if djtext[index] ==" " and djtext[index+1] ==" ":
                    pass
                else :
                    analyzed += char
            else:        
                if index != len(djtext)-1:
                    if djtext[index] ==" " and djtext[index-1] ==" ":
                        pass
                    else :
                        analyzed += char

        params = {'purpose':'Extra space remover', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params )  
    if charcount == "on":
        analyzed = 0
        for char in  djtext:
            analyzed += 1
        
        params = {'purpose':'Character counter', 'analyzed_text':analyzed}
        analyzed = 0
        return render(request,'analyze.html',params )

    else :
        return HttpResponse("<h1>Aandhe checkbox kon tick karega <h1>")















#----------------------------------------------------------------------------
# def removepunc(request):
#     a = '''<a href="/index">Home Page</a>'''
#     y = (request.GET.get('text','default'))
#     t = (a,"<br>","<br>","<h3>removepunc<h3>","<br> <br>",y)
#     return HttpResponse(t)

# def capfirst(request):
#     a = '''<a href="/index">Home Page</a>'''
#     t = (a,"<br>","<br>","<h3>capfirst<h3>")
#     return HttpResponse(t)

# def newlineremove(request):
#     a = '''<a href="/index">Home Page</a>'''
#     t = (a,"<br>","<br>","<h3>new line remover<h3>")
#     return HttpResponse(t)

# def spaceremove(request):
#     a = '''<a href="/index">Home Page</a>'''
#     t = (a,"<br>","<br>","<h3>space remover<h3>")
#     return HttpResponse(t)

# def charcount(request):
#     a = '''<a href="/index">Home Page</a>'''
#     t = (a,"<br>","<br>","<h3>charcount<h3>")
#     return HttpResponse(t)





















#-----------------------------basic----------------------------

# def myfav(request):
#     a_1 = '''<a href="https://www.youtube.com/">youtube</a>'''
#     a_2 = '''<a href="https://www.udemy.com/">udemy</a> '''
#     a_3 = '''<a href="https://www.programiz.com/python-programming/file-operation">python</a>'''
#     t = (a_1, '<br>', '<br>', a_2,'<br>','<br>', a_3)
#     return HttpResponse(t)



