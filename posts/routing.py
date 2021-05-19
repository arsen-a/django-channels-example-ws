from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/posts/', consumers.PostConsumer.as_asgi()),
]
