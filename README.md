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
capstone
├── capstone
│	├── _init_.py
│	├── asgi.py
│	├── settings.py
│	├── urls.py
│	└── wsgi.py
├── city3d
│	├── management/commands
│	│	├── *atx_permits.py (Retrieve JSON API data from Socrata, convert to pandas dataframe and upload to project database)
│	│	├── *security_key.py (Generate new Django security key for new users)
│	│	└── *sfo_permits.py (Retrieve JSON API data from Socrata, convert to pandas dataframe and upload to project database)
│	├── migrations
│	│	├── _init_.py
│	│	├── *0001_initial.py (Initial Django model migration to database)
│	├── static/city3d
│	│	├── buildings
│	│	│	├── Austin/img
│	│	│	│	├── *Block_185.jpg (Image for sample building)
│	│	│	│	└── *The_Republic.jpg (Image for sample building)
│	│	│	├── base
│	│	│	│	├── *pin_blue.gltf (Blue pin added to maps)
│	│	│	│	└── *pin.gltf (Red pin added to maps)
│	│	│	└── San Francisco/img
│	│	│		└── *655_Folsom.jpg (Image for sample building)
│	│	└── styles.css
│	├── templates/city3d
│	│	├── *city.html (3D map, renders individual cities)
│	│	├── *index.html (Homepage, base US map)
│	│	└── layout.html
│	├── _init_.py
│	├── admin.py
│	├── apps.py
│	├── models.py
│	├── tests.py
│	├── urls.py
│	└── views.py
├── *.env (Not included in github for security purposes, see instructions below)
├── .gitignore
├── *db.sqlite3 (Project database)
├── *README.md (Overview of project)
└── *requirements.txt (Packages required to run application)

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