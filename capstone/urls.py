from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('filter', views.filter, name="filter"),
    path('allParkings', views.allParkings, name="allParkings"),
    path('profile', views.profile, name="profile"),
    path('parking/<int:parking_id>', views.parking, name="parking"),
]