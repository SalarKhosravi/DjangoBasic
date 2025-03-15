## Basic django including, 
1. How to install django 
2. Basic commands, create project and create apps
3. Files and Folders structure 

<hr>


### 1. Installation (S02E02), visit [django installation document](https://docs.djangoproject.com/en/5.1/topics/install/#installing-official-release)

**On Mac, Linux**

```bash
  python -m venv .venv
  source .venv/bin/activate
    
  python -m pip install Django
```

**On Windows CMD**

```cmd
  py -m venv .venv
  .venv\Scripts\activate
    
  py -m pip install Django
``` 


<hr>

### 2. django-admin commands (S02E03)

#### 2.1. Create a new project

django-admin let us work with django engine. 
Here, following command will create a new django project 
with root app name of (`blog`)

```bash
  django-admin startproject blog
```

#### 2.2. Structure of a django project (S02E04)

- `manage.py` provides us a CLI to work with our project and its pieces

- `__init__.py` is an empty file that present the current folder as a python package

- `setting.py` is a file contains all configs in our django project

- `urls.py` is a file contained all the http routes of our project

- `wsgi.py` | `asgi.py` will be used in the deployment phase



#### 2.3. `manage.py` commands

To run the server and make the project live, we need to run by `manage.py`

```bash
  python manage.py runserver 8000
```


<hr>

### 3. django-admin commands (S02E06)

Apps in django act like modules that can get together and make
the full functionality of a web application. To create new app 
inside our project, we should use `manage.py` again

```bash
  python manage.py startapp posts
```

After this command, python will add a new directory 
to our projects that have multiple file. 

- `migrations` is the path where the database migrations will be saved
- `admin.py` aims to manage the display of models in admin side
- `apps.py` is the setting and config of the app
- `models.py` is the database structure of app
- `test.py` is for unit testing of the app
- `views.py` is a file that mange the request and response with parsing views