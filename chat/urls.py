from django.urls import path
from .views import *

app_name = 'chat'

urlpatterns = [
    path('', home, name="home"),
    path('search', search, name="search"),
    path('rooms', list_public_chat_rooms, name="list_rooms"),
    path('room/<slug:slug>', join_room, name="join_room"),
]