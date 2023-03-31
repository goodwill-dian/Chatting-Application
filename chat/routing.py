from django.urls import path
from . import consumers

websocket_urlpatterns = [
    # path('sc/', consumers.MySyncConsumer.as_asgi()),
    path('ac/', consumers.MyAsyncConsumer.as_asgi()),
]