from django.urls import path
from .views import TravelView, TravelCarView, TravelHotelView

app_name = 'travel'

urlpatterns = [
    path('travel/', TravelView.as_view(), name='travel'),
    path('travel/<int:pk>/', TravelView.as_view(), name='travel-detail'),

    path('travel/car/', TravelCarView.as_view(), name='travel_car'),
    path('travel/car/<int:pk>/', TravelCarView.as_view(), name='travel_car_detail'),

    path('travel/hotel/', TravelHotelView.as_view(), name='travel_hotel'),
    path('travel/hotel/<int:pk>/', TravelHotelView.as_view(), name='travel_hotel_detail'),
]
