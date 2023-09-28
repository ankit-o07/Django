"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
# os.environ.setdefault('SERVER_GATEWAY_INTERFACE', 'Asynchronous')
from home.consumers import *
from channels.auth import AuthMiddlewareStack
application = get_asgi_application()


ws_patterns = [
    path('/ws/test/',TestConsumer)
]

application = ProtocolTypeRouter({
    "http" : get_asgi_application(),
    'websocket' : AuthMiddlewareStack(
        URLRouter([ws_patterns])
    )
})

