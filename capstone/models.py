from django.db import models
from django.contrib.auth.models import AbstractUser

categories = (
    ('car', 'CAR'),
    ('motorcycle', 'MOTORCYCLE'),
    ('car and motorcycle', 'CAR AND MOTORCYCLE'),
)

yn = (
    ('Free', 'FREE'),
    ('Ocupied', 'OCUPIED')
)

# Create your models here.
class User(AbstractUser):
    pass

# class Slot(models.Model):
#     status = models.CharField(max_length=20, choices=yn, default="True")

#     class Meta:
#         abstract = True


#     def __str__(self):
#         return f'slot {self.id} is {self.status}'


class Parking(models.Model):
    title = models.CharField(max_length=140, default="unknown")
    category = models.CharField(max_length=20, choices=categories, default="car")
    img_src = models.CharField(max_length=200, default="../../static/capstone/img/parking4.jpg")
    # slots = models.ManyToManyField(Slot)
    slots = models.IntegerField()
    def __str__(self):
        return self.title

class Slot(models.Model):
    status = models.CharField(max_length=20, choices=yn, default="True")

    def __str__(self):
        return f'slot {self.id} of {self.status} is {self.available}'




 