from django.db import models
from django.contrib.auth.models import AbstractUser


categories = (
    ('car', 'CAR'),
    ('motorcycle', 'MOTORCYCLE'),
    ('car and motorcycle', 'CAR AND MOTORCYCLE'),
)


# Create your models here.
class User(AbstractUser):
    pass

class Parking(models.Model):
    title = models.CharField(max_length=140, default="unknown")
    category = models.CharField(max_length=20, choices=categories, default="car")
    img_src = models.CharField(max_length=200, default="../../static/capstone/img/parking4.jpg")
    slots = models.IntegerField()
    def __str__(self):
        return self.title
 