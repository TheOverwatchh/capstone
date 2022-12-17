from django.contrib import admin
from .models import User, Parking, Slot
# Register your models here.
admin.site.register(Parking)
admin.site.register(User)
# admin.site.register(Slot)

# superuser: micael micaelgomestargino@gmail.com micael123