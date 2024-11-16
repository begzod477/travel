from django.contrib import admin

from .models import TravelHotel, TravelCar, Travel

# Register your models here.

admin.site.register(TravelHotel)
admin.site.register(TravelCar)
admin.site.register(Travel)
