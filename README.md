# DJANGO TEMPLATE - IMAGINARY SHOP

You can use this template in your project.  
If you don't know Django. Here is a little tutorial  

## Install Django
```
pip install django
```
## Create Project

django-admin startproject (project name)

## Creating an app

-python manage.py startapp (app name)

## Link app to Project

-Go to setting.py in main project
-Find INSTALLED_APPS Array
-add app in array ("myapp")

## Create file in app

-urls.py

## Checking with HttpResponse

-Open view.py in app
-Add (HttpResponse) with "," in first line
-Write (
def home(request):
	return HttpResponse("Lorem Ipsum")
)

## Connecting to root

-Open urls.py
-Write (
from django.urls import path
from . import views

urlpatterns = [
	path("", views.home, name="home")
]
) in urls.py in app

## Connecting app to root

-open urls.py in project(default file)
-Add (include) with ","
-Write in urlpatterns (
	path("", include("myapp.urls"))
)

## Run the Server

-python manage.py runserver

## HTML Templates

-create folder in app (templates)
-create file base.html
-Write Html code using blocks
-create file home.html or somethingElse.html
-Write Html code using blocks

## Render templates

-Open views.py in app
-Update the code (
def home(request):
	return render(request, "home.html")
)

## Databases models

-Open models.py
