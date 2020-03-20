from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class owned_cars(models.Model):    
    make=models.CharField(max_length=20)
    car_image=models.ImageField(upload_to='car_pics')
    price_per_day=models.IntegerField()
    location=models.CharField(max_length=20)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.make
    
class bookings(models.Model):
    Pick_up_date=models.DateField()
    Return_date=models.DateField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    cars=models.ForeignKey(owned_cars,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user
    