## Introduction
> Welcome to Find Parking, a capstone project for `CS50'S Web Programming With Python and JavaScript` course. In this final project, using the python framework `Django` in the backend and  `JavaScript` in frontend, I intended to develop an app that could help the citizens and the parking owners to find and relate to each other, creating new parking lots, parking and finding parking lots in the city of the user, in order to make more easy to the citizens find where to park their cars when the traffic is caotic and help the parking owners to get more clients.

### distinctiveness and complexity
* First of all, I've just had to code in the other projects, because the the area of the app created, as well as the functionalities developed, were altogether given to us as requirements to complete the project. It didn't happen in this final project. I needed to put my imagination in action. Analyze the possibilities, the design, the user experience and the importance of each funcionality made me grow. I needed to transform my mind in an professional web developer mind. Needed to learn about the demands of the labor market, how to supply them and how to code way more smartly. 
* futhermore, in this project, desiring to offer the user a complete experience, I studied about the Google Maps JavaScript API and implemented it in this app. Not only this implementation counts as something different than the other projects, but counts too as something more complex, because i'm not interacting with local API'S, but with real, external and professional API'S in the web developing world, this relationship works in some aspects:
    * Making requests
    * Getting data
    * Processing each response
    * Manipulating the HTML DOM
    * Intervening events 
        - change in map zoom
        - change in map framing

* In adittion, this app counts with not only the functionalities of creating a parking, parking a vehicle or logging in/out, it counts too of the record of how many times the user did each of those things and the exact date and time it was made. This implementation makes the user experience more counscious and more safe, because, as an example, if the park manager try to receive the payment of the parking doubled, due to the time spent in the parking, the user has access to the log of each parking, including the time, the vehicle and the license plate.
* Last but not least, this project has something different than the other projects: when a parking owner tries to create a new parking lot, instead of copy the image web link in a input, now it's possible to click and load an image file inside the own device to be the image of the parking lot, making the user experience more pleasant, safe and easy.

### what's contained in each file
```
.
├── README.md
├── capstone
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── admin.cpython-38.pyc
│   │   ├── models.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   └── views.cpython-38.pyc
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── 0002_slot.py
│   │   ├── 0003_auto_20221217_1751.py
│   │   ├── 0004_delete_slot.py
│   │   ├── 0005_auto_20221219_2247.py
│   │   ├── 0006_user_times_logged.py
│   │   ├── 0007_auto_20221220_0314.py
│   │   ├── 0008_auto_20221220_1548.py
│   │   ├── 0009_auto_20221220_1559.py
│   │   ├── 0010_auto_20221220_1601.py
│   │   ├── 0011_parking_creator.py
│   │   ├── 0012_loghistory.py
│   │   ├── 0013_auto_20221220_1933.py
│   │   ├── 0014_auto_20221220_1944.py
│   │   ├── 0015_park.py
│   │   ├── 0016_remove_park_date.py
│   │   ├── 0017_auto_20221223_1604.py
│   │   ├── 0018_auto_20221223_1613.py
│   │   ├── 0019_auto_20221224_1208.py
│   │   ├── 0020_auto_20221224_1255.py
│   │   ├── 0021_parking_address.py
│   │   ├── 0022_auto_20221229_0002.py
│   │   ├── 0023_auto_20221229_0101.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-38.pyc
│   │       ├── 0002_slot.cpython-38.pyc
│   │       ├── 0003_auto_20221217_1751.cpython-38.pyc
│   │       ├── 0004_delete_slot.cpython-38.pyc
│   │       ├── 0005_auto_20221219_2247.cpython-38.pyc
│   │       ├── 0006_user_times_logged.cpython-38.pyc
│   │       ├── 0007_auto_20221220_0314.cpython-38.pyc
│   │       ├── 0008_auto_20221220_1548.cpython-38.pyc
│   │       ├── 0009_auto_20221220_1559.cpython-38.pyc
│   │       ├── 0010_auto_20221220_1601.cpython-38.pyc
│   │       ├── 0011_parking_creator.cpython-38.pyc
│   │       ├── 0012_loghistory.cpython-38.pyc
│   │       ├── 0013_auto_20221220_1911.cpython-38.pyc
│   │       ├── 0013_auto_20221220_1933.cpython-38.pyc
│   │       ├── 0014_auto_20221220_1911.cpython-38.pyc
│   │       ├── 0014_auto_20221220_1944.cpython-38.pyc
│   │       ├── 0015_park.cpython-38.pyc
│   │       ├── 0016_auto_20221221_1837.cpython-38.pyc
│   │       ├── 0016_remove_park_date.cpython-38.pyc
│   │       ├── 0017_auto_20221221_1859.cpython-38.pyc
│   │       ├── 0017_auto_20221223_1604.cpython-38.pyc
│   │       ├── 0018_auto_20221223_1613.cpython-38.pyc
│   │       ├── 0018_park_user.cpython-38.pyc
│   │       ├── 0019_auto_20221224_1208.cpython-38.pyc
│   │       ├── 0019_delete_park.cpython-38.pyc
│   │       ├── 0020_auto_20221224_1255.cpython-38.pyc
│   │       ├── 0021_parking_address.cpython-38.pyc
│   │       ├── 0022_auto_20221229_0002.cpython-38.pyc
│   │       ├── 0023_auto_20221229_0101.cpython-38.pyc
│   │       └── __init__.cpython-38.pyc
│   ├── models.py
│   ├── static
│   │   └── capstone
│   │       ├── createParking.css
│   │       ├── img
│   │       │   ├── background-login.png
│   │       │   ├── busy_city.jpg
│   │       │   ├── main-img-form.png
│   │       │   ├── parking.jpg
│   │       │   ├── parking2.jpg
│   │       │   ├── parking3.jpg
│   │       │   ├── parking4.jpg
│   │       │   ├── parking5.jpg
│   │       │   └── trafic-light.jpg
│   │       ├── index.css
│   │       ├── login.css
│   │       ├── map.js
│   │       ├── parking.css
│   │       └── profile.css
│   ├── templates
│   │   └── capstone
│   │       ├── allParkings.html
│   │       ├── atual_park.html
│   │       ├── createParking.html
│   │       ├── index.html
│   │       ├── layout.html
│   │       ├── login.html
│   │       ├── parking.html
│   │       ├── profile.html
│   │       └── register.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── finalproject
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── settings.cpython-38.pyc
│   │   ├── urls.cpython-38.pyc
│   │   └── wsgi.cpython-38.pyc
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── static
    └── capstone
        └── img
            ├── parking4.jpg
            └── parking5.jpg

```
### How to run the aplication

#### Be sure that you have the latest versions of python and django installed in your device.

1. Clone the following repository: <br> 
> <https://github.com/TheOverwatchh/capstone> <br>
2. In your terminal, open the directory which you saved the cloned repository.
3. run the codes below, in this order: <br>
`Python3 manage.py makemigrations` <br>
`Python3 manage.py migrate` <br>
`Python3 manage.py createsuperuser` <br>
`Python3 manage.py runserver` <br>
4. Make sure your browser has the permission to access your geographic location, it is needed to load the maps and the routes between the user and the parking lots.