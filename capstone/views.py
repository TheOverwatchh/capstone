from django.shortcuts import render
from django.core.paginator import Paginator 
from .models import  User, Parking

# Create your views here.
def login(request):
    return render(request, "capstone/login.html")

def logout(request):
    return render(request, "capstone/index.html")    

def register(request):
    return render(request, "capstone/register.html")

def index(request):
     return render(request, "capstone/index.html")

def allParkings(request):
     allParkings = Parking.objects.all().order_by('-id')

     paginator = Paginator(allParkings, 3)
     page_number = request.GET.get('page')
     posts_of_the_page = paginator.get_page(page_number)


     return render(request, "capstone/allParkings.html", {
        "allParkings": allParkings,
        "parkings_of_the_page": posts_of_the_page,
    })

def parking(request, parking_id):
    parking = Parking.objects.get(pk=parking_id)
    slots_n = parking.slots
    i = 0
    slots = ''
    while i < slots_n:
        slots += 'x'
        i +=1    
    return render(request, "capstone/parking.html", {
        "parking": parking,
        "slots": slots
    })          

def filter(request):
    return render(request, "capstone/index.html")

def profile(request):
    return render(request, "capstone/profile.html")    
