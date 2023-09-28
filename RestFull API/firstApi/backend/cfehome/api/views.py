from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.

def api_home(request, *args,**kwargs):

    body = request.body
    print(body)
    data = {}
    try:
        data= json.loads(body)
    except :
        pass 

    # print("\n\n\n")
    # print(data.keys)
    # print("\n\n\n")
    #data["headers"] = request.headers
    #print(request.GET)
    data['params'] = dict(request.GET)
    data["headers"] = dict(request.headers)
    data['content_type'] = request.content_type 
   #print(data)
    return JsonResponse(data)

