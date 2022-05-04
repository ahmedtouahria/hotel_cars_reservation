from django.urls import path
from .views import *
urlpatterns = [
    path("cars/",cars,name="cars"),
    path("cars/<int:pk>",car,name="car"),
    
]
