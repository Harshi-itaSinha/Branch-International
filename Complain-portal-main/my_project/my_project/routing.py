# routing.py

from django.urls import re_path
from ..customer import consumers

websocket_urlpatterns = [
    re_path(r'ws/admin_dashboard/$', consumers.ComplaintConsumer.as_asgi()),
]
