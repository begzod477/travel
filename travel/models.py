from django.db import models

# Create your models here.

class Travel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = "Sayohat"
        verbose_name_plural = "Sayohatlar"

    def __str__(self):
        return self.name

class TravelCar(models.Model):
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        verbose_name = "Sayohat mashinasi"
        verbose_name_plural = "Sayohat mashinalari"
        ordering = ['price']
    
    def __str__(self):
        return self.name
    
class TravelHotel(models.Model):
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE)
    name = models.CharField(max_length=55)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    hotel_stars = models.IntegerField()
    class Meta:
        verbose_name = "Mehmonxona"
        verbose_name_plural = "Mehmonxonalar"
        ordering = ['price']
    
    def __str__(self):
        return self.name



