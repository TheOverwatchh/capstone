from django.contrib import admin
from .models import User, Parking, Loghistory, Createparkhistory, Parkhistory, Park
# Register your models here.
admin.site.register(Parking)
admin.site.register(User)
admin.site.register(Loghistory)
admin.site.register(Createparkhistory)
admin.site.register(Parkhistory)
admin.site.register(Park)
