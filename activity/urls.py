from django.urls import path
from .views import *
urlpatterns = [
    path("activitys/",activitys,name="activitys"),
    path("activitys/<int:pk>",activity,name="activity"),
    
]
