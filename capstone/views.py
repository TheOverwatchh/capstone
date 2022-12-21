from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator 
from .models import Parking, User, Loghistory, Createparkhistory
from django.db import IntegrityError
from django.urls import reverse 
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
            # u.times_logged = u.times_logged + 1
            u.save() 
            allParkings = Parking.objects.all().order_by('-id')

            paginator = Paginator(allParkings, 3)
            page_number = request.GET.get('page')
            posts_of_the_page = paginator.get_page(page_number)

            
            l = Loghistory(logid=len(Loghistory.objects.all()) + 1, user=request.user)
            l.save()


            return HttpResponseRedirect(reverse('allParkings'))
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
        # u.times_logged = u.times_logged + 1
        u.save() 
        allParkings = Parking.objects.all().order_by('-id')

        paginator = Paginator(allParkings, 3)
        page_number = request.GET.get('page')
        posts_of_the_page = paginator.get_page(page_number)

        l = Loghistory(logid=len(Loghistory.objects.all()) + 1, user=request.user)
        l.save()

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

def createParking(request):
    if request.method == 'GET':
        return render(request, "capstone/createParking.html")
    else:
        title = request.POST['title']
        img_src = request.POST['img_src']
        slots = request.POST['slots']
        free_slots = slots
        unique = len(Parking.objects.all()) + 1
        category = request.POST['category']
        creator = request.user.username
        p = Parking(unique, title, category, img_src, slots, free_slots, creator)
        p.save()
        p_check = Parking.objects.get(pk=unique)
        if p_check:
            u = User.objects.get(username=request.user.username)
            # u.parks_created = u.parks_created + 1
            u.save()
            allParkings = Parking.objects.all().order_by('-id')
            paginator = Paginator(allParkings, 3)
            page_number = request.GET.get('page')
            posts_of_the_page = paginator.get_page(page_number)

            p = Createparkhistory(logid=len(Createparkhistory.objects.all()) + 1, user=request.user, park=Parking.objects.get(pk=unique))
            p.save()
            return render(request, 'capstone/allParkings.html', {
                "allParkings": allParkings,
                "parkings_of_the_page": posts_of_the_page,
            })
        return HttpResponseRedirect(reverse('allParkings'))

def deleteParking(request, parking_id):
     m = Parking.objects.get(pk=parking_id)
     m.delete()
     allParkings = Parking.objects.all().order_by('-id')

     paginator = Paginator(allParkings, 3)
     page_number = request.GET.get('page')
     posts_of_the_page = paginator.get_page(page_number)


     return HttpResponseRedirect(reverse('allParkings'))

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
    if request.method == 'POST':    
        category = request.POST['category']
        print(category)
        if category == 'both':
            allParkings = Parking.objects.all().order_by('-id')

            paginator = Paginator(allParkings, 3)
            page_number = request.GET.get('page')
            posts_of_the_page = paginator.get_page(page_number)
        else:
            allParkings = Parking.objects.filter(category=category).order_by('-id')

            paginator = Paginator(allParkings, 3)
            page_number = request.GET.get('page')
            posts_of_the_page = paginator.get_page(page_number)

        return render(request, "capstone/allParkings.html", {
            "allParkings": allParkings,
            "parkings_of_the_page": posts_of_the_page,
        })

    else:
        allParkings = Parking.objects.all().order_by('-id')

        paginator = Paginator(allParkings, 3)
        page_number = request.GET.get('page')
        posts_of_the_page = paginator.get_page(page_number)


        return render(request, "capstone/allParkings.html", {
            "allParkings": allParkings,
            "parkings_of_the_page": posts_of_the_page,        
   
        })

def profile(request):
    lgh = Loghistory.objects.filter(user=request.user).order_by('-logid')
    lghn = len(lgh)
    cph = Createparkhistory.objects.filter(user=request.user).order_by('-logid')
    cphn = len(cph)
    

    return render(request, "capstone/profile.html", {
        "lgh": lgh,
        "lghn": lghn,
        "cph": cph,
        "cphn": cphn
    })    
