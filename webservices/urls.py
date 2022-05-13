from django.urls import path
from .views import *
urlpatterns=[
   path("hotels/",HotelList.as_view(),) ,
   path("cars/",CarList.as_view(),) ,
   path("activitys/",ActivityList.as_view(),) ,

]