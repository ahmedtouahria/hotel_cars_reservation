from django.urls import path
from .views import *
urlpatterns = [
    path("",index,name="index"),
    path("rooms/",rooms,name="rooms"),
    path("rooms/<int:pk>",reserve,name="book_hotel"),
    
    
]
