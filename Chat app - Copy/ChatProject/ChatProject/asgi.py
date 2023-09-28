"""
ASGI config for ChatProject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
import chatApp.routing
from django.core.asgi import get_asgi_application
from channels.routing import  ProtocolTypeRouter , URLRouter
from channels.auth import AuthMiddlewareStack
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ChatProject.settings')
# os.environ.setdefault('SERVER_GATEWAY_INTERFACE', 'Asynchronous')

application = ProtocolTypeRouter({
    "http" : get_asgi_application(),
    'websockct' : AuthMiddlewareStack(
        URLRouter(
            chatApp.routing.websocket_urlpatterns
        )
    )

})


