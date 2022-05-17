from rest_framework import serializers
from hotel.models import Hotel
from cars.models import Car
from activity.models import Activity

# serialize hotel object to json 
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hotel
        fields="__all__"     
class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car
        fields="__all__"
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model=Activity
        fields="__all__"
