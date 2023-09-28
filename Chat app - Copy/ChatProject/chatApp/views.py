from django.shortcuts import render
import os
# Create your views here.

def messages_page(request):
    # if os.environ.get('SERVER_GATEWAY_INTERFACE') == 'Web':
    #     print("wsgi")
    # else:
    #     print("asgi")
    return render(request, "messages.html")