from django.db import models
from datetime import datetime, date
from django.contrib.auth.models import AbstractUser

categories = (
    ('car', 'CAR'),
    ('motorcycle', 'MOTORCYCLE'),
    ('both', 'BOTH'),
)

yn = (
    ('Free', 'FREE'),
    ('Ocupied', 'OCUPIED')
)

# Create your models here.
class User(AbstractUser):
    pass

class Parking(models.Model):
    title = models.CharField(max_length=140, default="unknown")
    category = models.CharField(max_length=20, choices=categories, default="car")
    img_src = models.CharField(max_length=200, default="../../static/capstone/img/parking4.jpg")
    slots = models.IntegerField(default=0)
    free_slots = models.IntegerField(default=0)
    creator = models.CharField(max_length=140, default="unknown")
    address = models.CharField(max_length=280, default="unknown")

    def __str__(self):
        return f"{self.title}"


class Loghistory(models.Model):
    logid = models.AutoField(primary_key=True, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_logged")    
    date = models.CharField(max_length=30, default="UNAVAILABLE DATE")

    def __str__(self):
         return f'{self.user} logged in {self.date}' 


class Parkhistory(models.Model):
    logid = models.AutoField(primary_key=True, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_parked")    
    park = models.ForeignKey(Parking, on_delete=models.CASCADE, related_name="park_parked")    
    date = models.CharField(max_length=30, default="UNAVAILABLE DATE")


    def __str__(self):
         return f'{self.user} parked at {self.park} in {self.date}' 


class Createparkhistory(models.Model):
    logid = models.AutoField(primary_key=True, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_creator")    
    park = models.ForeignKey(Parking, on_delete=models.CASCADE, related_name="park_creaed")    
    date = models.CharField(max_length=30, default="UNAVAILABLE DATE") 

    def __str__(self):
         return f'{self.user} created the {self.park} in {self.date}' 


class Park(models.Model):
    logid = models.AutoField(primary_key=True, default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_who_is_parking")
    category = models.CharField(max_length=15, default="unknown")
    licensePlate = models.CharField(max_length=8, default="aaaa0000")
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE, related_name="parking_that_is_being_parked")