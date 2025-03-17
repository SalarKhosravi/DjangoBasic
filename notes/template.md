## HTML Templates and Rendering data 

HTML file must be places in `templates/app_name/home.html` for each app in their own folders

### 1.  [Template System](https://docs.djangoproject.com/en/5.1/intro/tutorial03/#use-the-template-system)

First it is necessary to create an HTML file in `app_name/templates/app_name` folder, then
we must put the app_name in INSTALLED_APPS in `setting.py` to make django know our app. 
Also make sure the `APP_DIRS` is True in Template setting.

```django
#views.py
    from django.shortcuts import render
    
    def index(request):
        context = {id: 3}
        return render(request, "posts/index.html", context)
        # render(request, "app_name/file_name.html", context)
```

### 2- Template Directives ([Django Template Language](https://docs.djangoproject.com/en/5.1/ref/templates/language/))

Basically, we can access each python django variable using {{ var_name}} in HTML.
Yet there are many other directives.

#### 2-1- Filters ([link](https://docs.djangoproject.com/en/5.1/ref/templates/language/#filters))

To do an action on the value of a variable in HTML output, we can use filters such as
```django
    <p>{{ value|default:"nothing" }}</p>
    <p>{{ value|length }}</p>
    <p>{{ value|filesizeformat }}</p>
    <p>{{ value|date:"D d M Y" }}</p>
    <p>{{ value|dictsort:0  }}</p>
```

#### 2-2 Loop Tag
```django
    <ul>
    {% for post in posts %}
        <li>{{ post.title }}</li>
    {% empty %}
        <li>Sorry, no post in this list.</li>
    {% endfor %}
    </ul>
```

#### 2-3- If condition Tag
```django
    {% if is_loading %}
        wait please ...
    {% elif is_loaded %}
        here is your data
    {% else %}
        error occurred
    {% endif %}
```

#### 2-4- URL Tag
```django
# basic format
    {% url 'some-url-name' arg1=v1 arg2=v2 %}

# urls.py
# for more data we must send them in order
    path("post/<int:id>/", app_views.post, name="app-views-post")

# inside html
    {% url 'app-views-post' post.id %}

```

### 3- Template Inheritance ([link](https://docs.djangoproject.com/en/5.1/ref/templates/builtins/))

In case we have a global template that all static files
and basic schema of html come from this basic.html file, then we need first a folder in root 
directory name `templates` then, define the 
templates folder in setting

```django
TEMPLATES = [
	{
        'DIRS': [ BASE_DIR / 'templates' ]
    }
]
```

A basic.html file would be created that contains all repetitive parts,
another files will extend the basic.html files and add what they have extra

```django
    {% extends "base.html" %}

    {% block title %}My amazing blog{% endblock %}

    {% block content %}

        {% for entry in blog_entries %}
            <h2>{{ entry.title }}</h2>
            <p>{{ entry.body }}</p>
        {% endfor %}

    {% endblock %}
```

#### 3-1- Include HTML files 

We can add other partials by `include` function to make the basic file completed

```django
{% include "name_snippet.html" with person="Jane" greeting="Hello" %}
```


#### 3-2- Load static files 

##### 3-2-1 Global static

The same for `templates`, here we need to create a folder name `static` in root of django.
Later we need to inform django of this global static folder in setting

```python
STATICFILES_DIRS = [ BASE_DIR / 'static' ]
```
 
Then address the file in `base.html`

```django
# Load css globally from global static file
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
```


##### 3-2-2 in-app static
Any CSS or JS files as well as img files must be in the `static`
folder of app that is determined in setting. Named folder as name of 
app then static `posts/static/posts`

To load static files, we can do it in two ways, one with `block` and other with `load static`

##### 3-2-3- using block

```django
#parent
 {% block css %}{% endblock  %}

#child
{% block css %}
    {% load static %}
    <link rel="stylesheet" href="{% static 'posts/style.css' %}">
{% endblock %}

```


##### 3-2-4- using load static 
```django
# Load img
    {% load static %}
    <img src="{% static 'images/hi.jpg' %}" alt="Hi!">

# Load css
# assuming a user_stylesheet variable is passed to the template
    {% load static %}
    <link rel="stylesheet" href="{% static user_stylesheet %}" media="screen">
 
# load img with prefix
    {% load static %}
    <img src="{% get_static_prefix %}images/hi.jpg" alt="Hi!">
```

### 4- Context Processors ([link](https://docs.djangoproject.com/en/5.1/ref/templates/api/#built-in-template-context-processors))

Context processors are simply functions that add data in each and every page of app.
To have one, we need to create file name `myapp/context_processors.py` and then 
set a function there to return a dictionary.

```django
def site_name(request):
    return {'SITE_NAME': 'My Awesome Site'}
```

now variable name `SITE_NAME` is accessible everywhere, 
but it is necessary to tell django our processor

```django
#setting.py
    TEMPLATES = [
        {
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.request',
                    'myapp.context_processors.site_name',  # Add this line
                ],
            },
        },
    ]


#template HTML
    <h1>Welcome to {{ SITE_NAME }}</h1>

```


Django have many built-in `Context Processors` namely

```django
    {% csrf_token %}
    <p>{% trans "Hello, World!" %}</p>
    <p>Current path: {{ request.path }}</p>
    <img src="{% static 'images/logo.png' %}" alt="Logo">
    <p>Current Timezone: {{ TIME_ZONE }}</p>
    <img src="{{ MEDIA_URL }}profile_pics/user1.jpg" alt="User Profile">
```

More builtin variable in `django.template.context_processors.auth` as `Context Processors`

##### 1. Check user logged in

```html
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
{% else %}
    <a href="/login/">Login</a>
{% endif %}
```

##### 2. Check user permissions

```html
{% if perms.app_name.can_edit %}
    <p>You have permission to edit this.</p>
{% endif %}
```

##### 3. Flash messages in `django.contrib.messages`

```html
{% for message in messages %}
    <p>{{ message }}</p>
{% endfor %}
```

##### 4. Check if a user belongs to a specific group

```html
{% if "admin" in user.groups.all %}
    <p>You are an admin!</p>
{% endif %}
```