from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Travel, TravelCar, TravelHotel
from .serializer import TravelSerializer, TravelHotelSerializer, TravelCarSerializer

class TravelView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                travel = Travel.objects.get(pk=pk)
                serializer = TravelSerializer(travel)
                return Response(serializer.data)
            except Travel.DoesNotExist:
                return Response({'message': 'Travel not found'}, status=404)
        travels = Travel.objects.all()
        serializer = TravelSerializer(travels, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TravelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk=None):
        try:
            travel = Travel.objects.get(pk=pk)
        except Travel.DoesNotExist:
            return Response({'message': 'Travel not found'}, status=404)
        serializer = TravelSerializer(travel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk=None):
        try:
            travel = Travel.objects.get(pk=pk)
            travel.delete()
            return Response({'message': 'Travel deleted'}, status=204)
        except Travel.DoesNotExist:
            return Response({'message': 'Travel not found'}, status=404)

class TravelHotelView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                travel_hotel = TravelHotel.objects.get(pk=pk)
                serializer = TravelHotelSerializer(travel_hotel)
                return Response(serializer.data)
            except TravelHotel.DoesNotExist:
                return Response({'message': 'TravelHotel not found'}, status=404)
        travel_hotels = TravelHotel.objects.all()
        serializer = TravelHotelSerializer(travel_hotels, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TravelHotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk=None):
        try:
            travel_hotel = TravelHotel.objects.get(pk=pk)
        except TravelHotel.DoesNotExist:
            return Response({'message': 'TravelHotel not found'}, status=404)
        serializer = TravelHotelSerializer(travel_hotel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk=None):
        try:
            travel_hotel = TravelHotel.objects.get(pk=pk)
            travel_hotel.delete()
            return Response({'message': 'TravelHotel deleted'}, status=204)
        except TravelHotel.DoesNotExist:
            return Response({'message': 'TravelHotel not found'}, status=404)

class TravelCarView(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                travel_car = TravelCar.objects.get(pk=pk)
                serializer = TravelCarSerializer(travel_car)
                return Response(serializer.data)
            except TravelCar.DoesNotExist:
                return Response({'message': 'TravelCar not found'}, status=404)
        travel_cars = TravelCar.objects.all()
        serializer = TravelCarSerializer(travel_cars, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TravelCarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk=None):
        try:
            travel_car = TravelCar.objects.get(pk=pk)
        except TravelCar.DoesNotExist:
            return Response({'message': 'TravelCar not found'}, status=404)
        serializer = TravelCarSerializer(travel_car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk=None):
        try:
            travel_car = TravelCar.objects.get(pk=pk)
            travel_car.delete()
            return Response({'message': 'TravelCar deleted'}, status=204)
        except TravelCar.DoesNotExist:
            return Response({'message': 'TravelCar not found'}, status=404)
