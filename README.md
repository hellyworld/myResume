# myResume
## Project pre-installing:
* Install Atom from https://atom.io/
    * Atom packages
    * Atom-beautify
    * Platformio-ide-terminal
    * Atom-django
    * Autocomplete-python 
    * Django-templates
* Register to GitHub at https://github.com/

## Course 1
* Introduction
    * Check versions:
    ```
    python --version
    python -m django --version
    ```
    * About Django?
    Go to https://www.djangoproject.com/
    * What is Django?
    Django is a Python Web Framework
    * What is a Web Framework? /n
    Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.
    HTML, CSS, JS, bootstraps for responsive are integrated together, uploaded and hosted
    * What will me build?
    Open http://hellyworld.pythonanywhere.com/
    We will make an web app with our resume
* **Let’s build a project**
    * Create a new virtual environment
    Allow you to have a specific version of the packages: Python, Django, other API’s
    * Open a terminal in Atom
        * Move to .venvs folder
        * Create the new venv
        ```
        virtualenv myResume
        ```
    * Activate the new venv
    ```
    source .../myResume/bin/activate
    pip freeze
    ```
    * Install Django 2.1.3
    With Django , it actually also installed a command line tool called: django-admin (useful to quickly run direct from command line)
    ```
    pip install django
    pip freeze
    ```
    * Start a new project.
        * Move to projects folder
        * Start the new project
        ```
        django-admin startproject myResume
        ```
Project folders structure
myResume
__init__.py
This is a blank Python script that due to its special name let’s Python know that this directory can be treated as a package
settings.py
This is where you will store all your project settings
urls.py
This is a Python script that will store all the URL patterns for your project. Basically the different pages of your web application and how to connect to the end user. It use regular expressions.
wsgi.py
This is a Python script that acts as the Web Server Gateway Interface. It will later on help us deploy our web app to production.
manage.py
This is a Python script that will use a lot. It will be associates with many commands as we build our web app.
Will execute parts of django from your project.
Run a Django server
Move to myResume folder
```
python manage.py runserver
```
```
Performing system checks...

System check identified no issues (0 silenced).


You have 15 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, cont
enttypes, sessions.
Run 'python manage.py migrate' to apply them.

November 15, 2018 - 13:55:34
Django version 2.1.3, using settings 'first_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Copy to your browser and run http://127.0.0.1:8000/ and BIG CONGRATULATION TO YOU!
Warnings about migrations
A migrations allows you to move databases from one design to another, this is also reversible. You will migrate your database!
migrate your database
Create a superuser and access admin page
``` python
python manage.py createsuperuser
```
```
access http://127.0.0.1:8000/admin
```
```
python manage.py migrate
```
```
Operations to perform:
Apply all migrations: admin, auth, contenttypes, sessions

Running migrations:
Applying contenttypes.0001_initial... OK
Applying auth.0001_initial... OK
Applying admin.0001_initial... OK
Applying admin.0002_logentry_remove_auto_add... OK
Applying admin.0003_logentry_add_action_flag_choices... OK
Applying contenttypes.0002_remove_content_type_name... OK
Applying auth.0002_alter_permission_name_max_length... OK
Applying auth.0003_alter_user_email_max_length... OK
Applying auth.0004_alter_user_username_opts... OK
Applying auth.0005_alter_user_last_login_null... OK
Applying auth.0006_require_contenttypes_0002... OK
Applying auth.0007_alter_validators_add_error_messages... OK
Applying auth.0008_alter_user_username_max_length... OK
Applying auth.0009_alter_user_last_name_max_length... OK
Applying sessions.0001_initial... OK
Create a superuser and access admin page
python manage.py createsuperuser
access http://127.0.0.1:8000/admin
```

Setup proiect to use local_settings
local_settings.py
```python
from .settings import *
DEBUG = True
ALLOWED_HOSTS = ['*']
manage.py
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "resume.local_settings")
try:
from django.core.management import execute_from_command_line
except ImportError:
# The above import may fail for some other reason. Ensure that the
# issue is really that Django is missing to avoid masking other
# exceptions on Python 2.
try:
import django
except ImportError:
raise ImportError(
"Couldn't import Django. Are you sure it's installed and "
"available on your PYTHONPATH environment variable? Did you "
"forget to activate a virtual environment?"
)
raise
execute_from_command_line(sys.argv)
```
Save your venvs packages versions in a requirements.txt
```python
pip freeze > requirements.txt
pip install -r requirements.txt
```
GitHub - first repository
go to https://github.com/ and create a new repository myResume
install git
```
apt-get install git-core
```
.gitignore
build the file with https://www.gitignore.io/
git configuration
```git
git config --global user.name "hellyworld"
git config --global user.email "adrian.helerea@gmail.com"
git init
git remote add origin git@gitlab.com:hellyworld/myResume.git
README.md
git add .
git commit -m "Initial commit"
git push -u origin master
```
Course 2
Pull from GitLab
Start a new Django app
python manage.py startapp curriculum
App folders structure
curriculum
migrations
This directory stores database specific information as it relates to the models
__init__.py
This is a blank Python script that due to its special name let’s Python know that this directory can be treated as a package
admin.py
You can register your models here which Django will then use them with Django’s admin interface. Build into Django
apps.py
Here you can place application specific configurations
models.py
Here you store the application’s data models
tests.py
Here you can store test functions to test your code
views.py
This is where you have functions that handle requests and return responses
Configure the new app
Add the app to settings.py
Create mapping (urls, views, models and templates)
Simple mapping direct to a view
curriculum/views.py
Import HttpResponse object from django.hhtp module and each view for this application will exist in that views.py as it is own individual function. In this instance we created index function. Each function has at least one argument. As a conventional we call it “request but can be named whatever. Returns a HttpResponse  with a text later will be a html.
We need to map this view to the urls.py
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
return HttpResponse("Hello World!")

def resume(request):
return HttpResponse("This is my resume!")
urls.py
This is a Python script that will store all the URL patterns for your project. Basically the different pages of your web application and how to connect to the end user. It use regular expressions.
Django older than 2.0 format:
This is using regular expressions and link back
```python
from django.conf.urls import url
from django.contrib import admin
from curriculum import views

urlpatterns = [
url(r'^admin/', admin.site.urls),
url(r'^$', views.index, name='index'),
url(r'^resume/', views.resume, name=resume),
]
```
Django 2.0  format:

```python
from django.contrib import admin
from django.urls import path
from curriculum import views

urlpatterns = [
path('admin/', admin.site.urls),
path('', views.index, name='index'),
path('resume', views.resume, name='resume'),
]
```
Mapping with include()
Under this method each application will own a urls.py file and will keep our project’s urls.py clean and modular
urls.py
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path('admin/', admin.site.urls),
path('', include('curriculum.urls')),
]
```
curriculum/urls.py
```python
from django.urls import path
from curriculum import views

urlpatterns = [
path('', views.index, name='index'),
path('resume', views.resume, name='resume'),
]
curriculum/views.py
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
return HttpResponse("Hello World!")


def resume(request):
return render(request, 'resume.html')
Create mapping (urls, views, models and templates)
MTV (Model-Template-View) mapping
M stands for “Model,” the data access layer. This layer contains anything and everything about the data: how to access it, how to validate it, which behaviors it has, and the relationships between the data.
T stands for “Template,” the presentation layer. This layer contains presentation-related decisions: how something should be displayed on a Web page or other type of document.
V stands for “View,” the business logic layer. This layer contains the logic that accesses the model and defers to the appropriate template(s). You can think of it as the bridge between models and templates.


settings.py
TEMPLATES = [
{
'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': [os.path.join(BASE_DIR, 'templates')],
'APP_DIRS': True,
'OPTIONS': {
'context_processors': [
'django.template.context_processors.debug',
'django.template.context_processors.request',
'django.contrib.auth.context_processors.auth',
'django.contrib.messages.context_processors.messages',
],
},
},
]
urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path('admin/', admin.site.urls),
path('', include('first_app.urls')),
]
templates/base.html
Templates are a key part to understand how Django really works and interact with you website
Inside HTML we will use templates tags (Django Template Variable) with their special syntax
The syntax allows you to inject dynamic content that your Django  App’s views will produce, effecting the final HTML 
<!DOCTYPE html>
<html lang="en" dir="ltr">

<head>
<meta charset="utf-8">
<title></title>
</head>

<body>
<h1>This is my resume</h1>
</body>

</html>
models.py
Connect templates with models so you can  display data created dynamically from database
curriculum/urls.py
from django.urls import path
from first_app import views

urlpatterns = [
path('', views.index, name='index'),
path('resume', views.resume, name='resume'),
]
curriculum/views.py
Here we will create a dictionary that will have a content that will be injected  in HTML template. Takes in the key that will be the variable from html.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
return HttpResponse("Hello World!")


def resume(request):
my_dict = {
'insert_me': 'Hello there, I am from views.py'
}
return render(request, 'curriculum/resume.html')

curriculum/templates/curriculum/resume.html
This will help us to keep the project modular by create a subfolder for each app with their name
<!DOCTYPE html>
<html lang="en" dir="ltr">

<head>
<meta charset="utf-8">
<title></title>
</head>

<body>
<h1>This is my resume</h1>
<h3>{{ insert_me }}</h3>
</body>

</html>
Commit your work
Save your changes to GitHub
Course 3
Recap
Atom and python versions
Create a new virtual environment
Start a new project
Project folders structure
Run a Django server
Create a superuser to access admin
Setup project to use local_settings
Save your venvs packages versions in a requirements.txt
GitHub - first repository
Start a new app
Create mapping - single and with include()
Prepare the working environment
Activate your venv
Move to your project folder
Verify your repository
Pull from GitLab
The staticfiles app
https://docs.djangoproject.com/en/2.1/ref/contrib/staticfiles/
Staticfiles are files that will not change.
Here will be saved the CSS, JavaScript, images
create folder
static
css
my_style.css
images
django.jpeg
js
settings.py
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles', 'static_root')
STATICFILES_DIRS = [
os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'staticfiles', 'media_root')
resume.html
link your html files to static files by adding this tag {% load staticfiles %} at the top
insert a image use <img src="{% static 'images/django.jpeg' %}">
tag {{ }} is used for simple text injection
tag {% %} is used for more complex injections and logic
<!DOCTYPE html>
{% load staticfiles %}
<html lang="en" dir="ltr">
<head>
<meta charset="utf-8">
<title>{% block title %}Resume{% endblock %}</title>
<link rel="stylesheet" href="{% static 'css/my_style.css' %}">
</head>
<body>
<h1>This is my resume</h1>
<h3>{{ insert_me }}</h3>

<h3>Your picture is here!</h3>
<img src="{% static 'images/django.jpeg' %}" alt="django picture">
</body>
</html>
other useful tags
{% load staticfiles %}
{% block title %}Resume Adrian Helerea{% endblock  %}
{% block meta %}{% endblock %}
{% block jumbotron %}{% endblock %}
{% block content %}{% endblock %}
{% include "navbar.html" %}
{% extends 'base.html'%}
{% if request.user.is_authenticated %}
{% block content %}
<div class="container">
<p1 class=""> This is the Index One </p1>
{% if request.user.is_authenticated %}
<div class="container">
<iframe
src="https://calendar.google.com/calendar/embed?src=g7rn60hdn2ha2h37t3a60ignmg%40group.calendar.google.com&ctz=Europe%2FBucharest"
style="border: 0"
width="100%"
height="600"
frameborder="0"
scrolling="no">
</iframe>
</div>
{% endif %}
</div>

{% endblock %}
Collects the static files from all installed apps and copies them to the STATICFILES_STORAGE.
python manage.py collectstatic
Template extending
base.html
<!DOCTYPE html>
{% load staticfiles %}
<html lang="en" dir="ltr">

<head>
<meta charset="utf-8">
<title>{% block title %}My title{% endblock %}</title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
<link rel="stylesheet" href="{% static 'css/my_style.css' %}">
</head>

<body>
{% include 'jumbotron.html' %}

<h1>This is my Base.html</h1>

{% block content %}{% endblock %}

<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
</body>

</html>
index.html
{% extends 'base.html' %}

{% block content %}

<p>This is Resume! {{ insert_me }}</p>
<h4>My: {{ second }}</h4>

{% endblock %}
jumbotron.html
{% block jumbotron %}

<div class="container">
<div class="jumbotron">
<div class="row">
<div class="col-sm-6">
<h1 style="color:purple">Welcome to ScriuCod</h1>
{% if request.user.is_authenticated %}
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce sodales, nunc sit amet lobortis
viverra, purus metus pellentesque nisi, in ullamcorper quam orci in magna. Cras lacus quam,
ultricies sit amet arcu ut, interdum pellentesque diam. Cras tempus risus quis auctor tempus.</p>
{% else %}
<p>Please Logini</p>
{% endif %}
</div>
<div class="col-sm-6 text-center">
<div style="background-color:black; min-height:300px;">Video here</div>
</div>
</div>
</div>
</div>

{% endblock %}
Commit your work
Save your changes to GitHub
Course 4
Recap
Atom and python versions
Create a new virtual environment
Start a new project
Project folders structure
Run a Django server
Create a superuser to access admin
Setup project to use local_settings
Save your venvs packages versions in a requirements.txt
GitHub - first repository
Start a new app
Create mapping - single and with include()
Staticfiles App
Template extending
Prepare the working environment
Activate your venv
Move to your project folder
Verify your repository
Pull from GitLab
MTV (Model-Template-View)
M stands for “Model,” the data access layer. This layer contains anything and everything about the data: how to access it, how to validate it, which behaviors it has, and the relationships between the data.
T stands for “Template,” the presentation layer. This layer contains presentation-related decisions: how something should be displayed on a Web page or other type of document.
V stands for “View,” the business logic layer. This layer contains the logic that accesses the model and defers to the appropriate template(s). You can think of it as the bridge between models and templates.



Django Models
connect to SQlite3, Postgresql, MySQL
this class will be a subclass of Django built-in class: django.db.models.Model
each attribute of the class represents a field, which is just like a column name  with constraints in SQL
SQL is a giant table with each column represent a field ass CharField, IntegerField, DataField with constraints as max_length, default 
relationship between them and we use the concept of Foreign Keys and Primary Keys
Add libraries
django-ckeditor
https://django-ckeditor.readthedocs.io/en/latest/
pip install django-ckeditor



Create your Model
def __str__(self): is a method to return his actual name
from django.db import models
from ckeditor.fields import RichTextField


class Experience(models.Model):
company = models.CharField(max_length=50)
position = models.CharField(max_length=50)
location = models.CharField(max_length=50)
start_date = models.DateField()
end_date = models.DateField(blank=True, null=True)
description = RichTextField()

def __str__(self):
return self.company
migrate the database
this will create your database
python mange.py migrate
python manage.py makemigrations
relationship types
One-to-One
One-to-Many

Many-to-Many
Add Model to Admin
register your model to your app admin.py file
from django.contrib import admin
from curriculum.models import Experience

admin.site.register(Experience)
Add data to db from Admin
Generate a loop on class
Base.html
<!doctype html>
<html lang="en">
<head>
{% load staticfiles %}
<title>{% block title %}Resume Adrian Helerea{% endblock  %}</title>

<!-- Required meta tags -->
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<!-- Bootstrap CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.0.10/css/all.css" integrity="sha384-+d0P83n9kaQMCwj8F4RJB66tzIwOKmrdb46+porD/OvrJ+37WqIM7UoBtwHO6Nlg" crossorigin="anonymous">
<!--Custom CSS-->
<link rel="stylesheet" href="{% static 'css/resume.css' %}">
</head>
<body>

<div class="container">
{% include "navbar.html" %}
{% include "jumbotron.html" %}

<div class="container">
<div class="bpu afn afd">
<h2 class="bpv bpw" id="experience"><span class="fas fa-briefcase mr-2"></span>Experience</h2>
</div>
<div class="container">
{% include "experience.html" %}
</div>
</div>

<div class="container text-right text-muted">
<small>&copy; 2018 Copyrights: Adrian Helerea</small>
</div>
</div>
</body>
<!-- Optional JavaScript -->
<!-- jQuery first, then Popper.js, then Bootstrap JS -->
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<script src="{% static 'js/resume.js' %}"></script>
</html>
navbar.html
{% load staticfiles %}


<div class="container">
<nav class="nav navbar navbar-expand-lg navbar-dark fixed-top">
<div class="container">
<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
<span class="navbar-toggler-icon"></span>
</button>

<!--left side of navbar-->
<div class="collapse navbar-collapse" id="navbarCollapse">
<ul class="nav navbar-nav pull-sm-left">
<li class="nav-item">
    <a class="navbar-brand" href="#brand">
        Adrian Helerea
    </a>
</li>
<li class="nav-item">
    <a class="nav-link" href="#experience">
        <span class="fas fa-briefcase mr-2" aria-hidden="true"></span>Experience
    </a>
</li>
<li class="nav-item">
    <a class="nav-link" href="#education">
        <span class="fas fa-graduation-cap mr-2" aria-hidden="true"></span>Education
    </a>
</li>
<li class="nav-item">
    <a class="nav-link" href="#skills">
        <span class="fas fa-wrench mr-2" aria-hidden="true"></span>Skills
    </a>
</li>
<li class="nav-item">
    <a class="nav-link" href="#strength">
        <span class="fas fa-bolt mr-2" aria-hidden="true"></span>Strengths
    </a>
</li>
<li class="nav-item">
    <a class="nav-link" href="#contact">
        <span class="fas fa-paper-plane mr-2" aria-hidden="true"></span>Contact
    </a>
</li>
</ul>
</div>

<!--right side of navbar-->
<div>
<ul class="nav pull-sm-right">
<li class="nav-item">
    <a class="nav-link" href="mailto:helereaiadrian@gmail.com">
        <span class="fas fa-envelope" aria-hidden="true"></span>
    </a>
</li>
<li class="nav-item">
    <a class="nav-link" href="">
        <span class="fas fa-print" onclick="printPage()" aria-hidden="true"></span>
    </a>
</li>
<!--<li class="nav-item">-->
    <!--<a class="nav-link" href="#">-->
        <!--<span class="fas fa-cloud-download-alt" aria-hidden="true"></span>-->
    <!--</a>-->
<!--</li>-->
<li class="nav-item">
    <a class="nav-link" href="https://www.linkedin.com/in/adrianhelerea" target="_blank">
        <span class="fab fa-linkedin" aria-hidden="true"></span>
    </a>
</li>
</ul>
</div>
</div>
</nav>
</div>
Experience.html
{% load staticfiles %}


{% if all_experiences %}
{% for experience in all_experiences %}
<div class="container">
<div class="row">
<div class="col-md-8">
<h3>{{ experience.company }}</h3>
<h6>{{ experience.position }}</h6>
</div>
<div class="col-md-4">
<h6 class="text-sm-left text-md-right text-muted">{{ experience.location }}</h6>
<h6 class="text-sm-left text-md-right text-muted">{{ experience.start_date|date:'M Y'}} -
{% if experience.end_date is null %}
    Present
{% else %}
    {{ experience.end_date|date:'M Y'}}
{% endif %}
</h6>
</div>
</div>
<a data-toggle="collapse" href="#multi_collapse_experiece_{{ experience.id }}">
<i class="far fa-caret-square-down"></i>
Details
</a>
<div class="container collapse multi-collapse" id="multi_collapse_experiece_{{ experience.id }}">
{{ experience.description | safe}}
</div>
</div>
<br>
{% endfor %}
{% else %}
<h2>You don't have any experience, so please start your career!</h2>
{% endif %}
jumbotron.html
{% load staticfiles %}

<div class="container" id="brand">
<div class="jumbotron text-center pt-3">
<div class="row">
<div class="col-lg-4 mb-3 align-self-center">
<img src="static/img/AdrianHelerea.jpg" alt="Adrian" class="img-thumbnail">
</div>
<div class="col-lg-8 text-center">
<h1>Adrian Helerea</h1>
<blockquote>
<h5>"Be the change you wish to see in the world."</h5>
<footer class="blockquote-footer text-right">Mahatma Gandhi</footer>
</blockquote>

<h4 class="text-justify"><bolt>My objective:</bolt></h4>
<p class="text-justify">
I have been working in engineering for the last eight years, from Research Engineer in Silviculture
to Design Engineer in Storage Facilities, where I used Python to automate processes, and I am now
looking to fully transition as a Python Developer.
</p>
<p class="text-justify">
With strong ability of self taught and professional development, in the last year I studied and
worked to build web programs with Django and small scripts with Python and I am eager to improve my
Python skills in Computer Vision.
</p>
</div>
</div>
</div>
</div>
resume.css
@import url('https://fonts.googleapis.com/css?family=Roboto:400,700');

body {
color: #FFF;
background-color: #292b2c;
font-family: 'Roboto', sans-serif;
padding-top: 80px;
}

nav {
background-color: #292b2c !important;
font-variant: small-caps !important;
z-index: 10;
}

.navbar-brand {
display: inline-block;
padding-top: .3125rem;
padding-bottom: .3125rem;
margin-right: 1rem;
font-size: 1.25rem;
line-height: inherit;
white-space: nowrap;
color: #007bff !important;
}

.nav-link {
display: block;
padding: .5rem 0.8rem;
}

.navbar-dark .navbar-toggler {
border-color: #007bff !important;
}

.navbar-light .navbar-toggler {
border-color: #007bff !important;
}

.navbar-right {
margin: 0;
position: absolute;
right: 0;
top: 0;
}


.jumbotron {
padding: 2rem 2rem;
margin-bottom: 0rem;
color: #e9ecef;
background-color: #292b2c;
border-radius: 0.2rem;
}

.bpu {
position: relative;
line-height: 20px;
text-align: left;
font-variant: small-caps;
}

.bpu::before {
position: absolute;
top: 50%;
display: block;
content: "";
width: 100%;
height: 1px;
background-color: #e9ecef;
}

.bpv {
position: relative;
z-index: 2;
display: inline-block;
padding-left: 1rem;
padding-right: 1rem;
color: #e9ecef;
vertical-align: middle;
background-color: #292b2c;
}

.bpw {
margin-top: 0;
margin-bottom: 0;
color: inherit;
}

.afn, .afo {
margin-top: 3rem !important;
}

.afd, .afa {
margin-bottom: 2rem !important;
}

.fas, .fab, .FVIM {
color: #007bff;
}

.img-thumbnail {
padding: .25rem;
background-color: #fff;
border: 1px solid #dee2e6;
border-radius: 0.5rem;
max-width: 100%;
height: auto;
}
view.py
from django.shortcuts import render
from curriculum.models import Experience


def home(request):
all_experiences = Experience.objects.order_by("-id")
context = {
'all_experiences': all_experiences,
}

return render(request, 'base.html', context)
urls.py
from django.urls import path
from curriculum import views

urlpatterns = [
path('', views.home, name='home'),
]


Commit your work
Save your changes to GitHub
