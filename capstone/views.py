from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator 
from .models import Parking, User, Loghistory, Createparkhistory, Parkhistory, Park
from django.db import IntegrityError
from django.urls import reverse 
from datetime import datetime
from django.contrib.auth import authenticate, login as login_dj, logout as logout_dj
from PIL import Image
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

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            
            l = Loghistory(logid=len(Loghistory.objects.all()) + 1, user=request.user, date=dt_string)
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

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            
        l = Loghistory(logid=len(Loghistory.objects.all()) + 1, user=request.user, date=dt_string)
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
        img_srcn = f'/static/capstone/img/{img_src}'
        slots = request.POST['slots']
        address = request.POST['address']
        free_slots = slots
        unique = len(Parking.objects.all()) + 1
        category = request.POST['category']
        creator = request.user.username
        p = Parking(unique, title, category, img_srcn, slots, free_slots, creator, address)
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

            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

            p = Createparkhistory(logid=len(Createparkhistory.objects.all()) + 1, user=request.user, park=Parking.objects.get(pk=unique), date=dt_string)
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
    parks = Park.objects.filter(user=request.user, parking=parking)
    if len(parks) > 0:
        is_parked = True
    else: 
        is_parked = False 
    pp = Park.objects.filter(user=request.user)
    if len(pp) > 0:
        is_parked_anywhere = True
        whereParkedID = Park.objects.get(user=request.user).parking.id
    else:
        is_parked_anywhere = False
        whereParkedID = 0

    return render(request, "capstone/parking.html", {
        "parking": parking,
        "slots_n": slots_n,
        "slots": slots,
        "free_slots": free_slots,
        "free_slots_n": free_slots_n,
        "ocupied_slots_n": ocupied_slots_n,
        "ocupied_slots": ocupied_slots,
        "is_parked": is_parked,
        "is_parked_anywhere": is_parked_anywhere,
        "whereParkedID": whereParkedID
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
    parks = Parkhistory.objects.filter(user=request.user).order_by('-logid')
    parksn = len(parks)

    

    return render(request, "capstone/profile.html", {
        "lgh": lgh,
        "lghn": lghn,
        "cph": cph,
        "cphn": cphn,
        "parks":parks,
        "parksn":parksn 
    })    

def park(request):
    if request.method == 'POST':
        key = request.POST['parkingid']
        category = request.POST['category']
        licensePlate = request.POST['placa']
        p_n = len(Park.objects.all()) 
        unique = p_n + 1
        user = request.user
        parking = Parking.objects.get(pk=key)
        # check = len(Park.objects.filter(user=user))            
        # if check > 0:
            # parking = Parking.objects.get(pk=parking.id)
            # slots_n = parking.slots
            # free_slots_n = parking.free_slots
            # i = 0
            # slots = ''
            # while i < slots_n:
            #     slots += 'x'
            #     i +=1
            # free_slots = '' 
            # l=0 
            # while l < free_slots_n:
            #     free_slots += 'x'
            #     l +=1      
            # ocupied_slots_n = slots_n - free_slots_n
            # ocupied_slots = []
            # m = 0
            # while m < ocupied_slots_n:
            #     z = free_slots_n + (m + 1)
            #     ocupied_slots.append(z)
            #     m +=1 
            # slugid = Park.objects.get(user=user) 
            # slug = slugid.parking.id
            # return redirect(f'/parking/{parking.id}')      
        
        # if not check:            
        p = Park(logid=unique,user=user, category=category, licensePlate=licensePlate, parking=parking)
        p.save()
        ph_n = len(Parkhistory.objects.all())
        unique2 = ph_n + 1
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        ph = Parkhistory(logid=unique2, user=user, park=parking, date=dt_string)
        ph.save()
        parking.free_slots = parking.free_slots - 1
        parking.save()
        return redirect(f'/parking/{parking.id}#slots')      

def unpark(request):
    if request.method == 'POST':
        parking = Parking.objects.get(pk=request.POST['parkingid'])
        user = request.user
        park = Park.objects.filter(user=user, parking=parking)
        park.delete()
        parking.free_slots = parking.free_slots + 1
        parking.save()
        return redirect(f'/parking/{parking.id}#slots')

    p = Park.objects.filter(user=request.user)
    if len(p) > 0:
        return render(request, 'capstone/atual_park.html', {
            "is_there_a_park": 'Yes',
            "park": p
        })
    else:     
        return render(request, "capstone/atual_park.html", {
            'is_there_a_park': 'No'
        })       