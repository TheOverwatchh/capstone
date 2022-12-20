from django.shortcuts import render
from django.core.paginator import Paginator 
from .models import Parking, User
from django.db import IntegrityError
# from django.contrib.auth.models import User, 
from django.contrib.auth import authenticate, login as login_dj, logout as logout_dj
# Create your views here.
def login(request):
    if request.method == 'GET':
        return render(request, "capstone/login.html")
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_dj(request, user)
            u = User.objects.get(username=username)
            u.times_logged = u.times_logged + 1
            u.save() 
            allParkings = Parking.objects.all().order_by('-id')

            paginator = Paginator(allParkings, 3)
            page_number = request.GET.get('page')
            posts_of_the_page = paginator.get_page(page_number)


            return render(request, "capstone/allParkings.html", {
                "allParkings": allParkings,
                "parkings_of_the_page": posts_of_the_page,
            })
        else:
            return render(request, "capstone/login.html", {
                "message": "Invalid username and/or password."
            })
       
def register(request):
    if request.method == 'GET':
        return render(request, "capstone/register.html")  
    else:
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        typeof = request.POST['typeof']
        if typeof == 'park_manager':
            try:
                user = User.objects.create_user(username, email, password, is_staff=True)
                user.save()
            except IntegrityError:
                return render(request,'capstone/register.html', {
                    "message": "Username already taken."
                })    
        else:
            try:
                user = User.objects.create_user(username, email, password, is_staff=False)
                user.save()
            except IntegrityError:
                return render(request,'capstone/register.html', {
                    "message": "Username already taken."
                }) 
        login_dj(request, user) 
        u = User.objects.get(username=username, email=email)
        u.times_logged = u.times_logged + 1
        u.save() 
        allParkings = Parking.objects.all().order_by('-id')

        paginator = Paginator(allParkings, 3)
        page_number = request.GET.get('page')
        posts_of_the_page = paginator.get_page(page_number)


        return render(request, "capstone/allParkings.html", {
        "allParkings": allParkings,
        "parkings_of_the_page": posts_of_the_page,
    })               

def logout(request):
    logout_dj(request)
    return render(request, "capstone/index.html")    

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
    free_slots_n = parking.free_slots
    i = 0
    slots = ''
    while i < slots_n:
        slots += 'x'
        i +=1
    free_slots = '' 
    l=0 
    while l < free_slots_n:
        free_slots += 'x'
        l +=1      
    ocupied_slots_n = slots_n - free_slots_n
    ocupied_slots = []
    m = 0
    while m < ocupied_slots_n:
        z = free_slots_n + (m + 1)
        ocupied_slots.append(z)
        m +=1 
    return render(request, "capstone/parking.html", {
        "parking": parking,
        "slots_n": slots_n,
        "slots": slots,
        "free_slots": free_slots,
        "free_slots_n": free_slots_n,
        "ocupied_slots_n": ocupied_slots_n,
        "ocupied_slots": ocupied_slots,
    })          

def filter(request):
    return render(request, "capstone/index.html")

def profile(request):
    return render(request, "capstone/profile.html")    
