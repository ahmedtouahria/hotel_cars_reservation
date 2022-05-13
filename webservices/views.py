
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from hotel.models import Hotel
from cars.models import Car
from activity.models import Activity
from rest_framework import generics


class HotelList(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    def post(self, request, *args, **kwargs):
        return Response({"cannot create hotel"})
class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    def post(self, request, *args, **kwargs):
        return Response({"cannot create car"})
class ActivityList(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    def post(self, request, *args, **kwargs):
        return Response({"cannot create activity"})
    