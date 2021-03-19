"""
ASGI config for demo project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.urls import path
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from demo.apps.chat.consumers import ChatConsumer

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
                [path("ws/chat/<int:room_name>", ChatConsumer.as_asgi())]
            )
        ),
    }
)
