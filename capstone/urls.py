from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('filter', views.filter, name="filter"),
    path('allParkings', views.allParkings, name="allParkings"),
    path('createParking', views.createParking, name="createParking"),
    path('profile', views.profile, name="profile"),
    path('parking/<int:parking_id>', views.parking, name="parking"),
    path('park', views.park, name="park"),
    path('unpark', views.unpark, name="unpark"),
    path('atualPark', views.atualPark, name="atualPark"),
    path('deleteParking/<int:parking_id>', views.deleteParking, name="deleteParking"),
]