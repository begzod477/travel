from .models import Travel, TravelCar, TravelHotel
from rest_framework import serializers

class TravelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = '__all__'
    
    
    

class TravelCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelCar
        fields = '__all__'


class TravelHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelHotel
        fields = '__all__'
    