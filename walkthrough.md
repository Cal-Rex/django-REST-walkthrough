# Django REST | Building an API
_________________________________

## Contents

- API Concepts
    - revisit this video if you ever get stuck trying to understand structures and terminology when making an API
    - [video](https://youtu.be/IhUDroQO73w)

### Building a Profile API

#### Lesson 1: Api Profect Setup
1. [Setting up project with Django & Cloudinary on Github](#setting-up-project-with-django--cloudinary-on-github)
    - walkthrough: https://youtu.be/9BuhX2Tskbk
    - registering with cloudinary
    - Setting up a django project
    - configuring new project to use Cloudinary
2. [Adding a profiles App](#adding-a-profiles-app)
    - walkthrough: https://youtu.be/kic4oI2f1pM
    - creating the profiles app
        - [cheatsheet from CodeInstitute](https://docs.google.com/document/d/1i4ZZcV5B9g-a0gXZoxgmt7mhrqdizVOjXuT3-NGxiHg/edit)
    - writing the profiles model
    - using a signal method to create a profile
    - [Django signals explained](#django-signals)

-----------------------------

#### lesson 2: The Profile Resource
3. [REST Freamework Serializers](#rest-framework-serializers)
    - Walkthrough: https://youtu.be/V7KNSGrSLPg
    - how to write a class view to list all profiles
        - how to write a ProfileList
        - how to write an APIView
    - Learn what Serializers are and why they're useful
        - what the similarities are between ModelForms and ModelSerializers
    - how to write a profile model serializer
4. [Populating Serializer ReadOnly Field using dot notation]()
    - Walkthrough: https://youtu.be/e3sJYZ_UyBk
        - The `source` attribute and its string value explained
        - how to manipulate ReadOnlyFields (using dot notation)
            - targeting subfields within data models / tables
5. [GET and PUT requests (Profile Details view)](#get-and-put-requests-profile-details-view)
    - Walkthrough: https://youtu.be/uAyRQA4UIGY
    - How CRUD functionality maps to views and urls
    - The steps needed to write a profile view
    - [Stept needed to write the ProfileDetail class view.](#creating-the-profiledetail-view)
        - [GETting an existing profile](#retreiving-an-existing-profile)
        - [PUTting updated data into a profile](#updating-an-existing-profile)
6. [Authentication, Authorization and serializer method fields](#authentication-authorization-and-serializer-method-fields)
    - Walkthrough: https://youtu.be/bDfQdBL70oM
    - add in-browser login/logout feature
    - write custom permissions
    - add an extra field to an existing serailizer
        - [adding custom fields depending on the authentication of the user using a serializer](#adding-custom-fields-depending-on-the-authentication-of-the-user-using-a-serializer)

-----------------------------

#### lesson 3: The Post Resource
7. [creating the Post app, its base model and serializer]()
    - Challenge, no video
    - creating a serializer
    - Creating a post model
    - Cretaing a new App
8. [Adding Image Filters](#adding-image-filters)
    - modify a serializer to add filters to uploaded images
9. [Creating the PostList View](#creating-the-postlist-view)
    - Walkthrough: https://youtu.be/BIaoKcYvr_M
    - create the PostList view and write two methods 
        1. ‘get’, to list all posts
        2. ‘post’ to create a user post
10. [Creating the Post Detail view](#the-post-detail-view)
    - Walkthrough: https://youtu.be/4poMrjNqqf4





__________________________________

## Setting up project with Django & Cloudinary on Github
##### https://youtu.be/9BuhX2Tskbk

this section covers:
- registering with cloudinary
- Setting up a django project
- configuring new project to use Cloudinary

1. create a new repo on [github](www.github.com)
- or, use the Codeinstitute full template: [https://github.com/Code-Institute-Org/ci-full-template](https://github.com/Code-Institute-Org/ci-full-template)
2. install Django via the CLI
    - `pip3 install django`
    - for this walkthrough, the LTS (Long Term Support) version of cjango was used. to use this, use:
        - `pip3 install 'django<4'`
3. Start a new project in the repo with django called `drf_api`, using the following command:
    - `django-admin startproject drf_api .`
        - the `.` initializes the project in the current directory
4. next, install cloudinary into the project with the following command:
    - `pip install django-cloudinary-storage`
5. install `Pillow`.
    - this library adds image processing capabilities that we need for this project. Note that it’s name starts with a capital P.
    - `pip install Pillow`
6. import the newly installed cloudinary apps (`cloudinary_storage` and `cloudinary`) into `settings.py` > `INSTALLED_APPS[]`
    - be sure to place `cloudinary_storage` **BEFORE** `django.contrib.staticfiles`
    - add `cloudinary` to the bottom of the `INSTALLED_APPS` list.
    - example of what `INSTALLED_APPS` should look like:
        ```py
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'cloudinary_storage',
            'django.contrib.staticfiles',
            'cloudinary'
        ]
        ```
7. set up `env.py` and the cloudinary environment variable
    - create a new `env.py` file
    - make sure it is included in `.gitignore`
    - add `import os` to the top of the file
    - set an environ for cloudinary using the cloudinary API key found on your cloudinary account page
        `os.environ['CLOUDINARY_URL'] = 'cloudinary://[REMOVE_THIS_AND_ADD_YOUR_API_KEY]@[REMOVE_THIS_AND_ADD_YOUR_CLOUD_NAME]'`
    - make an offline copy of your `env.py` file, incase you have to make a fresh workspace
8. next, set up a conditional in `settings.py` that if `env.py` exists, import it into settings.py
    - place this directly below `from pathlib import Path` at the tp of the file
    -   ```py
        import os

        if os.path.exists('env.py'):
            import env
        ```
9. beneath that code, retreive the cloudinary environment as an object inside a variable called `CLOUDINARY_STORAGE`:
    - `CLOUDINARY_STORAGE = {'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')}`
10. then, beneath that, define a setting for where media files will be stored:
    - `MEDIA_URL = '/media/'`
11. lastly, beneath that, add a default file storage setting:
    - `DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'`

top of `setting.py` should now look like this:
```py
from pathlib import Path
import os

if os.path.exists('env.py'):
    import env

CLOUDINARY_STORAGE = {'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')}
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'SECRET_KEY_REMOVED_LOL'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary'
]
```

_________________________________________________________

## Adding a Profiles app
##### https://youtu.be/kic4oI2f1pM

this section covers:
- creating the profiles app
- writing the profiles model
- using a signal method to create a profile
- [Django signals explained](#django-signals)
- [cheatsheet from CodeInstitute](https://docs.google.com/document/d/1i4ZZcV5B9g-a0gXZoxgmt7mhrqdizVOjXuT3-NGxiHg/edit)

1. create the new app with the `startapp` command:
    - `python3 manage.py startapp profiles`
        - (`python3 manage.py startapp YOUR_APP_NAME_HERE`)
2. with the new app created, it also needs to be included in `INSTALLED_APPS` in `settings.py`:
    -   ```py
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'cloudinary_storage',
            'django.contrib.staticfiles',
            'cloudinary',
            'profiles'
        ]
        ```
3. now, in the newly created `models.py` inside `profiles.py` add a new import at the top of the file:
    - `from django.contrib.auth.models import User`
4. next, inside `models.py` create the first new database model:
    -   ```py
        class Profile(models.Model):
            owner = models.OneToOneField(User, on_delete=models.CASCADE)
            created_at = models.DateTimeField(auto_now_add=True)
            updated_at = models.DateTimeField(auto_now=True)
            name = models.CharField(max_length=255, blank=True)
            content = models.TextField(blank=True)
            image = models.ImageField(
                upload_to='images/' default='../samples/landscapes/girl-urban-view'
            )

            class Meta:
                ordering = ['-created_at']
            
            def __str__(self):
                return f"{self.owner}'s profile"
        ```

##### django signals

- event notifications
    > You can think of signals as notifications that get triggered by an event.
- can listen to the events and run a piece of code every time
    > We can listen for such Model events and have some code, usually a function, run each time that signal is received.
- we'd like to create a user profile every time a user is created
    > In our case, we would want to be notified when a user is created so that a profile can automatically be created alongside it. 
- built-in model signals:
    - pre save: `pre_save`
    - post save: `post_save`
    - pre delete: `pre_delete`
    - post delete `post_delete`

to implement:
1. import the `post_save` signal from `django.db.models.signals` at the top of `models.py`
    - `from django.db.models.signals import post_save`
2. now, beneath the `Profile` class model, add a call to `post_save`appended with the `.connect()` function, passing 2 arguments:
    - the first argument will be `create_profile`, which is the function that needs to be run every time a post is saved. 
    - the second is going to be specifiying who/what is the sender of the new data, in this case, it will be the `User` 
    - `post_save.connect(create_profile, sender=User)`
3. now, above this call, define the `create_profile` function:
    - the function has to take 4 arguments: `(sender, intance, created, **kwargs)`
    - set a conditional statement that if a profile is created, the owner of the profile should be that `User`
    - the function should look like this:
    -   ```py
        def create_profile(sender, instance, created, **kwargs):
                    # Because we are passing this function 
                    # to the post_save.connect method
                    # it requires the following arguments:
                    # 1. the sender model,
                    # 2. its instance
                    # 3. created  - which is a boolean value of 
                    #    whether or not the instance has just been created
                    # 4. and kwargs.  
                    if created:
                        # if created is True, we’ll create a profile  
                        # whose owner is going to be that user.
                        Profile.objects.create(owner=instance)
                
        # not part of the function, but this would be sitting
        # directly under it
        post_save.connect(create_profile, sender=User)
        ```
        > now every time a user is created, a signal will trigger the Profile model to be created.
4. register the `Profile` model in `admin.py` so that it will show up in the admin panel
    - `admin.site.register(Profile)`
5. before going any further, migrate the new model into the database in the CLI:
    - `python3 manage.py makemigrations`
    - `python3 manage.py migrate`
6. now, to view the model on the admin panel:
    - first create a superuser/admin
        - `python3 manage.py createsuperuser`
        - create a username and password from the command prompts
        - no need to supply an email address
7. run the server and go to admin and see if everything is working:
    - `python3 manage.py runserver`
    - append `/admin` to the url in the browser window and login with the admin credentials
    - be sure to add the workspcae url as an `ALLOWED_HOST` in `settings.py`

> Now, if we run our server, and go to /admin, we see that our first user was created. And their corresponding profile was created with a working image, well done!

8. finally, create a file containing the new project's dependencies via the CLI
    - `pip freeze > requirements.txt`
9. push the changes to github

_________________________________________________________________

## REST Framework Serializers
##### https://youtu.be/V7KNSGrSLPg

- how to write a class view to list all profiles
    - how to write a ProfileList
    - how to write an APIView
- Learn what Serializers are and why they're useful
    - what the similarities are between ModelForms and ModelSerializers
- how to write a profile model serializer

How Model Serializers work:
- similar to Django's `ModelForms`, they handle validation
- Uses similar syntax to `ModelForms`:
    - can use `Meta` class
    - can specify extra fields.
    - can use `.is_valid()` and `.save()` methods
    - Handle all the conversions between different data types

> we need a serializer to convert Django model instances to JSON. As we’ll only be working with Django Models, we’ll use model serializers to avoid data replication, just like you would use ModelForm over a regular Form. Before we write a model serializer, let’s talk a bit more about what they are: they are very similar to Django’s ModelForms, in that, they handle validation. The syntax for writing a model serializer is the same, we specify the model and fields in the  Meta class and we can specify extra fields too. We can use methods like .is_valid  and .save with serializers Additionally, they handle all the conversions between different data types.



1.  install `djangorestframework` in the CLI
    - `pip3 install djangorestframework`
    - add it to `INSTALLED_APPS` in `settings.py` below `cloudinary`, but above any manually created apps like `Profiles`
        - `'rest_framework',`
        -   ```py
            INSTALLED_APPS = [
                'django.contrib.admin',
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.messages',
                'cloudinary_storage',
                'django.contrib.staticfiles',
                'cloudinary',
                'rest_framework',
                
                'profiles'
            ]
            ```
2. create the first view in `views.py`, start by importing everything needed
    - import `APIView` from `rest_framework.views` at the top of `views.py`
        - `from rest_framework.views import APIView`
    -    > APIView is very similar to Django’s View  class. It also provides a few bits of extra functionality such as making sure you receive Request instances in your view, handling parsing errors, and adding context to Response objects.
    - import `Response` from `rest_framework.response`
        - `from rest_framework.response import Response`
    -    > Even though we could use Django’s HttpResponse, the Response class is specifically built for the  rest framework, and provides a nicer interface for returning content-negotiated Web API responses  that can be rendered to multiple formats.
    - import the `Profile` database model from `models.py`
         - `from .models import Profile`
3. next, use the imported `APIView` view to create a class view called `ProfileList`
    - inside it, define a get request that puts all objects in the `Profiles` table into a variable called `profiles`
    - then, in the return statement, return a `Response` with the parameter of the `profiles` variable 
    -   ```py
        class ProfileList(APIView):
            def get(self, request):
                profiles = Profile.objects.all()
                return Response(profiles)
        ```
4. map the new view to a URL in `urls.py` in the `profiles` app
    - first, import `path` from `django.urls`
    - import the `profiles` argument established in the `return Response` from `views.py`
        -   ```py
            from django.urls import path
            from profiles import views
            ```
    - next, create the `urlpatterns` list variable, and write a path for `profiles/` that renders the `ProfileList` view as a view (`as_view()`)
        -   ```py
            urlpatterns = [
                path('profiles/', views.ProfileList.as_view()),
            ]
            ```
5. map the newly made url pattern in `profiles/urls.py` into the urls of `drf_api`
    - at the top of `drf_api/urls.py` add `include` to the imports from `django.urls`
        - `from django.urls import path, include`
    - use the newly imported `include` method to write in a new path for `profiles.urls` in `drf_api/urls.py`'s `urlpatterns`
        -   ```py
            from django.contrib import admin
            from django.urls import path, include

            urlpatterns = [
                path('admin/', admin.site.urls),
                path('', include('profiles.urls')),
            ]
            ```
    > Now, if we start the server, and go to ‘profiles/’, we get an ugly error: Object of type Profile is not JSON serializable. Let's have a look at what’s happening and why we’re seeing this error. 

    > When a user posts data to our API, the following has to happen: we need that data to be deserialized, which means it needs to be converted from a data format like JSON or XML to Python native data types. 

    > Then, we have to make sure the data is valid (just like with Django forms) once it’s validated, a model  instance is saved in the database.

    > If our users are requesting data from our API, a queryset or model instance is returned from the database. It is then converted to Python native data types before the data is sent back, it is converted again, or serialized to a given format (most commonly JSON). 
    
    > This is the reason we saw the error. The profiles can’t be just thrown in as a part of the Response, we need a serializer to convert Django model instances to JSON.  

6. create a new file, `serializers.py` in the `profiles` app.
7. in the new file, import the following:
    - `serializers` from `rest_framework`
    - `Profile` from `.models`
    -    ```py
        from rest_framework import serializers
        from .models import Profile
        ```
8. create a class with the name `ProfileSerializer` that inherits from `serializers.ModelSerializer` and create a `ReadOnlyField` from `serializers` called `owner`, it should contain the parameter `source='owner.user`
    - give it a `Meta` class and specify the following fields to include in the response
        - `model = Profile`
        - `fields = []`
            - the value for fields can be determined in 2 ways:
            - > You could list them  all in an array or set to ‘__all__’ like this, however I prefer to be explicit about which  fields I am including, because I might want to add another field to my Profile model later  on, that I don’t want included in the serializer.
                1. `fields = '__all__'`
                2. `fields = ['id', 'owner', 'created_at', 'updated_at', 'name', 'content', 'image']`
                    - > Please note, that when extending Django's model class using models.models, the id field is created automatically without us having to write it ourselves. If we want it to be included in the response, we have to add it to the serializer's field array.
    -   ```py
        from rest_framework import serializers
        from .models import Profile

        class ProfileSerializer(serializers.ModelSerializer):
            owner = serializers.ReadOnlyField(source='owner.username')

            class Meta:
                model = Profile
                fields = [
                    'id',
                    'owner',
                    'created_at',
                    'updated_at',
                    'name',
                    'content',
                    'image'
                ]
        ```

9. return to `views.py` and import the newly made `ProfileSerializer` class
    - `from .serializers import ProfileSerializer`
10. then, in the `ProfileList` class in `views.py`, add a new instance called `serializer`, which makes a call to the newly imported `ProfileSerializer` class at the top of the file, it should contain 2 arguments:
    1. first should be the `profiles` variable containing `all` the `Profile` `objects`
    2. second, should be `many=True` to specify that multiple profile instances are to be serialized
11. in the return statement of `ProfileList`, update the `response` parameter with the value of `serializer.data`
    -   ```py
        from django.shortcuts import render
        from rest_framework.views import APIView
        from rest_framework.response import Response
        from .models import Profile
        from .serializers import ProfileSerializer

        class ProfileList(APIView):
            def get(self, request):
                profiles = Profile.objects.all()
                serializer = ProfileSerializer(profiles, many=True)
                # this takes the objects in profiles and runs it through the
                # ProfileSerializer defined in serializers.py
                # it takes this data, then takes the `Profile` model as a reference
                # and then renders the specified fields within the passed-in
                # dataset into JSON data
                return Response(serializer.data)
        ```
12. check this is all working by running the preview and appending the preview url with `/profiles/`
    - `python3 manage.py runserver`
    - if running correctly, a django REST page should appear, displaying JSON data objects of all the profiles existing within the app. 
    - > we can see the array being returned in a nice user  interface created by rest framework. If we click on the GET json button, we’ll see plain JSON,  which is exactly what a React application would see. Our serializer has taken the Python data and converted it into JSON, which is ready for the front end content to use! 
    
13. > Before we finish, let’s update our dependencies.
    - update `requirements.txt` in the terminal
        - `pip3 freeze > requirements.txt`

_____________________________________________________________________

## Populating Serializer ReadOnly Field using dot notation
##### https://youtu.be/e3sJYZ_UyBk


- The `source` attribute and its string value explained
- how to manipulate ReadOnlyFields (using dot notation)
    - targeting subfields within data models / tables

Entity relationship between the `User` table that comes with Django, and the `Profile` table created in this project:

> The User and Profile tables are connected through the owner OneToOne field.

> By default, the owner field always  returns the user’s id value.

|       US | ER      | < - > |     PRO | FILE     |
| -------: | :------ | :---: | ------: | :------- |
|          |         |       | id      | BigAuto  |
|       id | BigAuto |  -- > | owner   | OneToOne |
| username | Char    |       | name    | Char     |
| password | Char    |       | content | Text     |
|          |         |       | image   | Image    |

> For readability’s sake, however, every time we fetch a profile, it makes sense to overwrite this default behaviour  and retrieve the user’s username instead.  

|        US|ER       | < - > |      PRO|FILE      |
| -------: | :------ | :---: | ------: | :------- |
|       id | BigAuto |       | id      | BigAuto  |
| username | Char    |  -- > | owner   | OneToOne |
| password | Char    |       | name    | Char     |
|          |         |       | content | Text     |
|          |         |       | image   | Image    |

> To access this field, we use dot notation.

**inside serializers.py, in the `ProfileSerializer` class**
```py
owner = serializers.ReadOnlyField(
    source='owner.username'
)
```
> In this case, the “owner” in “owner.username”  stands for the user instance, so any time we want to access a field we simply use dot notation.  

basically `owner` can act as a direct call to that specific user, and using dot notation from `owner` would be the same as `User.AWAYTOIDENTIFYASPECIFICUSER.WHATEVERFIELD`

Now, lets add a 3rd table for `posts`

|        US|ER       | < - > |       PO|ST           | < - > |      PRO|FILE      |
| -------: | :------ | :---: | ------: | :---------- | :---: | ------: | :------- |
|       id | BigAuto |       |      id | BigAuto     |       | id      | BigAuto  |
| username | Char    | < - > |   owner | Foreign Key | < - > | owner   | OneToOne |
| password | Char    |       |   title | Char        |       | name    | Char     |
|          |         |       | content | Text        |       | content | Text     |
|          |         |       |   image | Image       |       | image   | Image    |

> Let’s assume we are working  on PostSerializer instead of ProfileSerializer like we did in the previous video.

In these tables, `Post.owner` is a `ForeignKey` field, this means if the there was a serializer serializing information from `Post`, the name of a user could be found by dot notation, by going through `owner`(which is targeting the user through it being na instance) then `Profile`, so the dot notation would be `owner.Profile.name`.

```py
class PostSerializer(serializers.ModelSerializer):
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.name'
    )
```

> One last challenge. Let’s say we wanted to add the profile image field to each post.

|        US|ER       | < - > |       PO|ST           | < - > |      PRO|FILE      | subfields |
| -------: | :------ | :---: | ------: | :---------- | :---: | ------: | :------- | :-------: |
|       id | BigAuto |       |      id | BigAuto     |       | id      | BigAuto  |           |
| username | Char    | < - > |   owner | Foreign Key | < - > | owner   | OneToOne |           |
| password | Char    |       |   title | Char        |       | name    | Char     |           |
|          |         |       | content | Text        |       | content | Text     |           |
|          |         |       |   image | Image       |       | image   | Image    | url       |

Because the `profile.image` field comtains a "subfield" housing the `url` for the image, that needs to be targeted directly in the dot notation.

```py
class PostSerializer(serializers.ModelSerializer):
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.image.url'
    )
```

______________________________________________________________________

## GET and PUT requests (Profile Details view)
##### https://youtu.be/uAyRQA4UIGY

This section covers:
- How CRUD functionality maps to views and urls
- The steps needed to write a profile view
- Stept needed to write the ProfileDetail class view.

Profiles CRUD Table:
> Let’s have a look at our CRUD table. It shows what kind of HTTP request our users have to make and to which URL in order to list all profiles, create, read, update or delete the profile. 

| HTTP           | URI           | CRUD Operation                                                                   | View Name         |
| :------------: | :-----------: | :------------------------------------------------------------------------------: | :---------------: |
| **a**.GET / **b**.POST | /profiles     | **a**.list all profiles / **b**.create a profile                         | LIST              |
| **c**.GET / **d**.PUT / **e**.DELETE | /profiles/:id | **c**.retrieve a profile by id / **d**.update a profile by id / **e**.delete a profile by id | DETAIL           |

quick recap reference to the ProfileList view to help write the next code:
```py
class ProfileList(APIView):
    """
    List All profiles
    No Create view (POST method), as profile creation is
    handles by Django signals
    """
    def get(self, request):
        profiles = profile.objects.all()
        serializer = ProfileSerializer(profles, many=True)
        return Response(serializer.data)
```
while this class handles `GET`ting a list of all profiles, it doesn't `POST` data/create new profiles.
This is because profile creation is handled by [django signals](#django-signals), referenced earlier.

there is still no: 
- `GET` method to retreive a specific profile by id
- view or methods to utulise `PUT`, which updates data (a profile) by id

### creating the `ProfileDetail` view

the view needs to:
1. fetch the profile by id
2. serialize the profile model instance
3. return serializer data in the response
    - ([serializer](#rest-framework-serializers) needed to turn the data into JSON format)


#### Retreiving an existing profile
steps:
1. Go to `views.py`
2. create a new class called `ProfileDetail` that inherits from the [imported `APIView`](#rest-framework-serializers)
3. create a `get_object` request that takes `self` and `pk` (PrimaryKey) as arguments
    - this function not only has to try and retreive a data record by the parameters above, it also needs to handle the instance of when a record doesnt exist
    - because of this, add an except/exception block by using the `try` keyword
    - inside the block, add a variable called profile that queries the `objects` of `Profile` to `get` a record where `pk` = the `pk` entered in the request.
    -   ```py
        class ProfileDetail(APIView):
            def get_object(self, pk):
                try:
                    profile = Profile.objects.get(pk=pk)
                    return profile
        ```
    - this handles the instance of where the record exists, now the code needed to handle the exception needs to be added 
4. Create the code that handles the event of a record not existing
    - at the top of the file (`views.py`), import `Http404` from `django.http`
        - `from django.http import Http404`
    - then, back in the `ProfileDetail` class, add an `except` statement to the `try` statement.
        - this is structured like `if`/`else`
        - the `except`ion should handle the event of `Profile.DoesNotExist`
        - the action it takes in this event is to `raise` a call to `Http404`
        -   ```py
            class ProfileDetail(APIView):
                def get_object(self, pk):
                    try:
                        profile = Profile.objects.get(pk=pk)
                        return profile
                    except Profile.DoesNotExist:
                        raise Http404
            ```
5. now that the records have been checked to make sure the profile exists, the queried profile now needs to be serialized:
    - beneath the `get_object` request, write a new `get` request that takes `self`, the `request`, and `pk` (primary key) as arguments
    - create a variable called `profile` with the value being the `get_object` function declared above, being called on it`self`, taking the `pk` as the argument
        - `profile = self.get_object(pk)`
    - create a variable called `serializer`, its value should be a call to the [`ProfileSerializer`](#rest-framework-serializers) with the `profile` variable as its argument
        - > unlike in `ProfileList` No need to pass in many=True, as unlike last time, we’re dealing with a single profile model instance and not a queryset.
    - with the profile now serialized, return it in the `Response` for the `get` request:
    -   ```py
        class ProfileDetail(APIView):
            def get_object(self, pk):
                try:
                    profile = Profile.objects.get(pk=pk)
                    return profile
                except Profile.DoesNotExist:
                    raise Http404
            
            def get(self, request, pk):
                profile = self.get_object(pk)
                serializer = ProfileSerializer(profile)
                return Response(serializer.data)
        ```
6. test that this code is working by adding the `DetailView` to the `urlpatterns` in `urls.py`:
    - under the list view, add a new `path` that takes the arguments of:
        - the path for the url as a string value that calls the the `profiles` path, but then in `<>` the `pk` as an `int`eger, suffixed with a `/`
            - `'profiles/<int:pk>/'`
        - the `ProfileDetail` view from `views` as a view, using `as_view()`
            - `views.ProfileDetail.as_view()`
    -   ```py
        urlpatterns = [
            path('profiles/', views.ProfileList.as_view()),
            path('profiles/<int:pk>/', views.ProfileDetail.as_view())
        ]
        ```
    - run the app to see if it all works.
        - `python3 manage.py runserver`


#### Updating an existing profile
process:
1. fetch the profile by it's id
    - > First, we’ll have to retrieve the  profile using the get_object method. 
2. call the serializer with the profile and request data
    - > Next, we’ll have to call our serializer with that instance and data that’s being sent in the request.
3. if data is valid, save and return the instance
    - > Then, we’ll call .is_valid on our serializer, just like we would on a form, to make sure the data is valid. If it is, we’ll save the updated profile to the database and return it in the Response. In case it isn’t, we’ll have to return a 400 BAD REQUEST error.

steps:
1. inside the `profileDetail` class in `views.py`, define a `put` request that takes `self`, the `request` and the `pk` (PrimaryKey) as arguments
    - define the `profile` variable again like in the `get` request, where the variable's value is running the `get_object` function on it`self`, taking the `pk` as an argument
    - define the serializer variable again using the `ProfileSerializer` as its value, this time though, it should take 2 arguments:
        - `profile`
        - `data=request.data` which is taking the form data from the request passed in
    - now check `if` the value of `serializer` `is_valid()`, with an `if statement`, if it is, `save()` `serializer`
    - `return` a `Response` with the parameter of the `serializer`'s `data`
    - instead of an `else` statement, add a `return` statement in place of an `else` statement, which `return`s a `Response` with 2 arguments:
        1. any `errors` created by the `serializer`
        2. a `status` parameter imported from `rest_framework`, that has the value of `status.HTTP_400_BAD_REQUEST`
            - be sure to - `from rest_framework import status` - at the top of `views.py`
    -   ```py
        def put(self, request, pk):
            profile = self.get_object(pk)
            serializer = ProfileSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        ```

> Ok, that's all! Let’s make sure our new  view is working! If we go to ‘profiles/id/’, we’ll see PUT among the allowed HTTP methods.  We’ll also have a text area in which we could write raw JSON to update the profile. But wouldn’t it be better to have a nice form instead?

2. make the newly created form in the ProfileDetail view contextual by setting the `serializer_class` to `ProfileSerializer` in the `ProfileDetail` class, as the first line under the class definition:
    - this tells the `APIView` template being used by `ProfileDetail` to follow the field structure of the `ProfileSerializer` for its forms
    -   ```py
        class ProfileDetail(APIView):
            # establish the form structure for the data
            serializer_class = ProfileSerializer

            def get_object(self, pk):
                """
                the function that checks the validity
                of a profile request, returns an error if
                invalid
                """
                try:
                    profile = Profile.objects.get(pk=pk)
                    return profile
                except Profile.DoesNotExist:
                    raise Http404
            def get(self, request, pk):
                """
                uses the function above to get a profile by id
                serializes it using the ProfileSerializer
                """
                profile = self.get_object(pk)
                serializer = ProfileSerializer(profile)
                return Response(serializer.data)

            def put(self, request, pk):
                """
                updates a retreived profile with data receieved
                from a request via a form contextualised by
                serializer_class at the top of this view
                handles BAD_REQUEST errors too
                """
                profile = self.get_object(pk)
                serializer = ProfileSerializer(profile, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        ```

_______________________________________________________________________

## Authentication, authorization and serializer method fields
##### https://youtu.be/bDfQdBL70oM

This section covers:
- add in-browser login/logout feature
    - > make it possible to log  in and log out of our API in-browser interface
- write custom permissions
    - > write the IsOwnerOrReadOnly permission
- add an extra field to an existing serailizer
    - > add an extra field to our Profile Serializer

> We’ll do all this so that only the owner of  a profile can edit it and not just any user.


before getting started on the steps above, create another superuser, so that there are 2 accounts to work with:
- in the terminal:
    1. `python3 manage.py createsuperuser`
    2. follow terminal prompts

user created:

| Username | Password |
| -------: | :------- |
| admin2   | guest    |


with that done, begin createing the ligon/logout views:

These come as part of the native REST framework package:
1. add a new path to `drf_api/urls.py` that takes `api-auth/` as the path name, and uses the `include` import to include `'rest_framework.urls'`
    -   ```py
        from django.contrib import admin
        from django.urls import path, include

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('api-auth/', include('rest_framework.urls')),
            path('', include('profiles.urls')),
        ]
        ```
2. run the server and check to see if the new path works:
    - on the `/profiles/` page, there should now be a dorpdown in the top right of the page allowin users to logout/login

however, regardless of who is logged in, any user can update a record, which is not ideal.

> Luckily, not only does the rest framework come with a set of commonly used permissions, like `AllowAny`, `IsAuthenticated`, `IsAdminUser`, `IsAuthenticatedOrReadOnly` and more; it also makes it very easy to write custom permissions (`BasePermission` - used to write custom permissions)


### Creating a Custom permission

requirements for a custom permission:
1. > It has to be an object-level permission, which means we’ll have to check a Profile model instance object and see if its ‘owner’ field is  pointing to the same user who’s making the request.
2. > If the user is requesting read-only access using the so-called safe http  methods, like GET, return True.
3. > If the user is making a PUT or PATCH request, return True only if that user owns the profile object.

**steps:**
1. create a new file in `drf_api` called `permissions.py`
2. at the top of the file, import `permissions` from `rest_framework`
    - `from rest_framework import permissions`
3. then, create a new class called `IsOwnerOrReadOnly` that inherits from `permisssions.BasePermission`
    - `class IsOwnerOrReadOnly(permissions.BasePermissions):`
4. overwrite the pre-existing function `has_object_permission` supplied by the inherited import. it takes 4 arguments `(self, request, view, obj)`
    - this is done by just writing it as a new function
5. in the function:
    - add an `if` statement that checks if the `method` in the `request` argument is `in` the `SAFE_METHODS` of `permissions`. If it is, `return` a value of `True`
        - this checks to see if the user accessing the record is only requetsing Read-Only access, and if they are, the `True` result is returned
    - directly under it, in lieu of an `else` statement, add a `return` statement that has a conditional checking that `owner` in the `obj` argument matches the `request`ing `user`
        - this checks to see if the user owns that record and will return a `True` value if they match.
    -   ```py
        class IsOwnerOrReadOnly(permissions.BasePermisssions):
            def had_object_permission(self, request, view, obj):
                if request.method in permissions.SAFE_METHODS:
                    return True
                return obj.owner == request.user
        ```
6. with the permission written, it can now be used in `views.py`, import it at the top of the `views.py file`:
    - `from drf_api.permissions import IsOwnerOrReadOnly`
7. now that it is imported, permissions classes can be added to views by using the variable `permission_classes` which passes an array of all of the necessary permissions. In this case, there is only one, so pass it in as a single entry within an array/list. Add the following variable to the `ProfileDetail` view, below the `serializer_class` variable:
    - `permission_classes = [IsOwnerOrReadOnly]`
8. next, inside the `ProfileDetail` view, the `get_object` function now needs to be amended to make the function check the permissions of the accessing user:
    - > if the user doesn’t own the profile, it will throw the 403 Forbidden  error and not return the instance.
    - in the `try` statement, beneath the profile variable, run the function `check_object_permissions` on `self` with the arguments of `request` made by `self` and the `profile` variable established directly above it
        - `self.check_object_permissions(self.request, profile)`
    -   ```py
        class ProfileDetail(APIView):
        # establish the form structure for the data
        serializer_class = ProfileSerializer

        def get_object(self, pk):
            """
            the function that checks the validity
            of a profile request, returns an error if
            invalid
            """
            try:
                profile = Profile.objects.get(pk=pk)
                self.check_object_permissions(self.request, profile)
                return profile
            except Profile.DoesNotExist:
                raise Http404
        def get(self, request, pk):
        ```

> now, if we don’t own the profile, we aren’t allowed to make changes to it.


### adding custom fields depending on the authentication of the user using a serializer

1. go to `profiles/serializers.py`
    - > We’re going to use the  SerializerMethodField, which is read-only. It gets its value by calling a  method on the serializer class, named `get_<field_name>` (in this case, it will be `get_is_owner`).
2. in the `ProfileSerializer` class, add a new variable called `is_owner` under the `owner` variable
    - this variable will house the `SerializerMethodField` from the `serializers` import with no parameters.
        - `is_owner = serializers.SerializerMethodField()`
            - `SerializerMethodField()` is read-only
3. this new variable is then run like a function by prefixing the variable name with `get_` and defining it like a function, it will take `self` and `obj` as parameters

> we’d like to do something similar to what we did in our permission file, that is: check if request.user is the same as the object's owner. But there’s a problem. The currently logged in user is a part of the request object.

This information isn't currently directly available to the serializer in this file. So it needs to be passed into the serializer from `views.py`

> inside views.py, we’ll have to pass  it in as part of the context object when we call our ProfileSerializer inside our view. We’ll have to do it every time we call it.

4. first, add a new variable into the `get_is_owner` function called `request`, its value should be `self`'s `context`, where it targets the array value of `'request'` within itself
    - this `context` needs to be created as a parameter when the serializer is called in `views.py`, but this can be added after the rest of the function is built to save jumping back and forth
5. with the `request` variable now housing the `context`ual `request` from the `user`, this can be checked against the target object to see if the `user` matches the `obj`'s `owner`
    - under the `request` write a `return` statement that has a conditional statement to reflect this:
        -   ```py
            def get_is_owner(self, obj):
                request = self.context['request']
                return request.user == obj.owner
            ```
6. now, as mentioned before, the request information needs to be sent in the `context` value from `views.py` every time this serializer is called. to do that, go to `views.py`
7. wherever `serializer = ProfileSerializer(...)` is classed as a variable, a parameter of `context` needs to be added to the parameters, its value needs to be an object KVP with a key of `'request'` with the value of `request`
    - `serializer = ProfileSerializer(profiles, many=True, context={'request': request})` (for accessing multiple records)
    - `serializer = ProfileSerializer(profiles, context={'request': request})` (for accessing a single record)
    - example:
        -   ```py
            def put(self, request, pk):
                """
                updates a retreived profile with data receieved
                from a request via a form contextualised by
                serializer_class at the top of this view
                handles BAD_REQUEST errors too
                """
                profile = self.get_object(pk)
                # serailizer updated below
                serializer = ProfileSerializer(
                    profile,
                    data=request.data,
                    context={'request': request}
                )
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            ```
8. Lastly, include the new `'is_owner'` field in the `fields` array listed in the `Meta` class of `ProfileSerializer`
9. test that it all works

code should look like this:
```py
from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
        # this variable above is used to house 
        # the requisite serializer it is called 
        # as a function below by prefixing the variable's 
        # name with 'get_'

    def get_is_owner(self, obj):
        """
        passes the request of a user into the serializer
        from views.py
        to check if the user is the owner of a record
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            'id',
            'owner',
            'created_at',
            'updated_at',
            'name',
            'content',
            'image',
            'is_owner'
        ]
```

__________________________________________________________

## Setting up the Post App resources
#### Challenge

### Cretaing a new App
run the command in the terminal to make a new app, name it `posts`
    - `python3 manage.py startapp posts`

### Creating a post model
1. in `posts/models.py` import the following:
    - `models` from `django.db`
    - `User` from `django.contrib.auth.models`
    ```py
    from django.db import models
    from django.contrib.auth.models import User
    ```

2. create a class called `Post`, it should inherit from `models.Model`
3. the new `Post` class needs the following fields:
    - owner, which should be a `ForeignKey` using the `User` as its value, it should also `CASCADE` delete any related sub-items if deleted
    - created_at, which should be a `DateTimeField` which should be automatically assigned a new value upon record creation by using the parameter `auto_now_add=True`
    - updated_at, same as above, except its paramater is `auto_now=True`, not `auto_add_now` as it updates every time the post is edited, not when it is `add`ed
    - title, should be a `CharField` with a `max_length`
    - content, should be a `TextField` to house post content, it should be `blank` initially
    - image, which should be an `ImageField`. 
        - upon a successful upload, the image should be `upload`ed`_to` `'images/'` 
        - it should also have a default value from the cloudinary database using a static filepath
        - it should also be `blank` on the form
4. add a `Meta` class that orders posts by the `DateTime` they were `created_at`, with the most recent entry being first
5. define a dunder `str` methos that returns a python `f` string that contains the `id` and `title` of each post through the use of `this`

the post model should look like this:
```py
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../samples/landscapes/girl-urban-view', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
```

6. Migrate the completed model into the database
    1. `python3 manage.py makemigrations`
    2. `python3 manage.py migrate`


### creating a serializer

1. create a new file in `posts` called `serializers.py`
2. inside the new `serailizers` import:
    - `serializers` from `rest_framework`
    - the `Post` model from `.models`
3. create a class called `PostSerializer` which inherits from `serializers.ModelSerializer`
4. establish the following serailizer fields:
    - owner: a `ReadOnlyField` that's `source` is the `username` of the `owner` specified in the `Post` model
    - profile_id: a `ReadOnlyField` that's `source` is the `id` of the `owner` specified in the `Post` model (`id`'s are automatically created by django)
    - profile_image: a `ReadOnlyField` that's `source` is the `url` of the `image` field beonging to the `owner`, specified in the `Post` model
    - is_owner: a variable which houses the `SerializerMethodField` for the `serializer`
5. use the `is_owner` field to create a method (prefix it with `get_`) with the following parameters: `self` and `obj` for object in question
    - the function should then take a `context`ual `request` from whatever calls it (`this`), and then checks if the `user` that made the `request` matches the `obj`'s `owner`, `return`ing a voolean value depending on the outcome
6. add a `Meta` class that:
    - determines the `model` the serializer its basing its structure from, n this case it is `Post`
    - determine the `fields` it serializes and displays in a list variable as strings, they should be:
        - id
        - owner
        - created_at
        - updated_at
        - title
        - content
        - image

finished serializer shuold look like this:
```py
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.id')
    profile_image = serializers.ReadOnlyField(source='owner.image.url')
    is_owner = serializers.SerializerMethodField()
        # this variable above is used to house 
        # the requisite serializer it is called 
        # as a function below by prefixing the variable's 
        # name with 'get_'
    
    def get_is_owner(self, obj):
        """
        passes the request of a user into the serializer
        from views.py
        to check if the user is the owner of a record
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'id',
            'owner',
            'profile_id',
            'profile_image',
            'created_at',
            'updated_at',
            'title',
            'content',
            'image',
            'image_filter',
            'is_owner',
        ]
```

_____________________________________________

## Adding image filters
#### https://youtu.be/atHYnt2LLO4

this section covers:
1. Adding an image_filter field to the Post model
    - > add an  extra field to our Post model, called image_filter, to store the name of the filter to be applied to an image. 
2. validating post image
    - size
    - width
    - height
    - > add a mechanism to  validate user uploaded images. Our API will reject them if the image’s size, width, or height exceeds the limit we set.

            It is always a good idea to  have such checks in place.  
            It will help us to keep the network latency down, 
            make it easier for our  server to process the images, 
            stay within image hosting (cloudinary) platform’s free tier plan, 
            and display images properly  both in a web and mobile app. 

### 1. adding an image_filter
1. go to `posts/models.py`
2. > let’s go to our Post model. Inside the Post class, we’ll have to define the list of available choices for the image_filter character field.  
    - the following field was supplied by the tutorial, listing some stock filters in django:
        ```py
        image_filter_choices = [
            ('_1977', '1977'), ('brannan', 'Brannan'),
            ('earlybird', 'Earlybird'), ('hudson', 'Hudson'),
            ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'),
            ('kelvin', 'Kelvin'), ('normal', 'Normal'),
            ('nashville', 'Nashville'), ('rise', 'Rise'),
            ('toaster', 'Toaster'), ('valencia', 'Valencia'),
            ('walden', 'Walden'), ('xpro2', 'X-pro II')
        ]
        ```
    - add this as a variable above the established fields (directly below the class declaration)
    - > As you can see, the list consists of a series of  tuples. The first value is the actual string saved in the database and the second one is the value displayed in the dropdown menu in the in-browser interface.
3. create a new `image_filter` field using a `CharField` with `max_length` of `32` and a `choices` parameter consisting of the `image_filter_choices` variable prviously established above the fields variables. it should also have a `default`parameter of `'normal'`

```py
from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    image_filter_choices = [
        ('_1977', '1977'), ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'), ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'), ('normal', 'Normal'),
        ('nashville', 'Nashville'), ('rise', 'Rise'),
        ('toaster', 'Toaster'), ('valencia', 'Valencia'),
        ('walden', 'Walden'), ('xpro2', 'X-pro II')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../samples/landscapes/girl-urban-view',
        blank=True
    )
    image_filter = models.CharField(
        max_length=32,
        choices=image_filter_choices,
        default='normal'
        )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
```

4. migrate the updated model:
    1. `python3 manage.py makemigrations`
    2. `python3 manage.py migrate`


5. > and add the newly created image_filter field to our serializer fields.
    - go to `posts/serializers.py`
    - add `'image_filter'` to the `fields` list variable in the `PostSerializer`'s `Meta` class


### Validating post Image
> For that, we’ll use the rest framework’s field level validation methods. They’re called: `validate_<fieldName>`  

1.  go to `posts/serializers.py`
2. create a function using the `validate_` prefix:
    - > In our case the field name is ‘image’, so our method’s name will be `validate_image`.
    - pass it 2 arguments:
        - `self`, which is the instance
        - `value`, which is the uploaded image
        - make it `return` the `value` parameter
    - > **If we follow this naming convention, this method will be called automatically and validate the uploaded image every time we create or update a post.**
3. inside the function, add an `if` statement that:
    - if the `size` of `value` is greater than `1024 * 1024 * 2`, `raise` a `ValidationError` from `serializers` that passes a statement of:
        - `'Image size larger than 2MB!'`
        - > file size unit is a byte. If we multiply it by 1024, we’ll get kilobytes. Multiplied again by 1024, we’ll get megabytes. Now all we have to do is multiply it by two and we’ll get the 2 megabyte file size limit.
4. add another `if` statement that checks the `width` `value` of the `image` that `raise`s another `ValidationError` that passes the statement:
    - `'Image larger than 4096px'`
5. repeat the process above for the `height` `value` of the `image`

```py
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.id')
    profile_image = serializers.ReadOnlyField(source='owner.image.url')
    is_owner = serializers.SerializerMethodField()
        # this variable above is used to house 
        # the requisite serializer it is called 
        # as a function below by prefixing the variable's 
        # name with 'get_'
    
    def get_is_owner(self, obj):
        """
        passes the request of a user into the serializer
        from views.py
        to check if the user is the owner of a record
        """
        request = self.context['request']
        return request.user == obj.owner
    
    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image wider than 4096 pixels!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image taller than 4096 pixels!'
            )
        return value

    class Meta:
        model = Post
        fields = [
            'id',
            'owner',
            'profile_id',
            'profile_image',
            'created_at',
            'updated_at',
            'title',
            'content',
            'image',
            'image_filter',
            'is_owner',
        ]
```

__________________________________________________________________________

## Creating the PostList View
##### https://youtu.be/BIaoKcYvr_M


overview:
- create the PostList view and write two methods 
    1. ‘get’, to list all posts
    2. ‘post’ to create a user post


### Creating the PostList view
1. go to `posts/views.py`
2. import the following:
    -   ```py
        from django.shortcuts import render
        from rest_framework import status
        from rest_framework.response import Response
        from rest_framework.views import APIView
        from .models import Post
        from .serializers import PostSerializer
        ```
3. create the `PostList` class, it should inherit from `APIView`

### define the get method to list all posts
1. `def`ine the `get` method, which whould take 2 arguments: `self` and `request`
2. inside the `get` request, create a variable called `posts` that retrieves `all()` `objects` from `Post`
3. create the `serializer` variable that houses the `PostSerializer` established in `serializers.py`. pass it:
    - the `posts` variable
    - the `many` parameter, set to `True`
    - `context`, which has a {K: V} Pair of K: `'request'` V: `request`
4. have the function `return` a `response`, its parameter being the serialized `data` of the `serializer` variable
    ```py
    from django.shortcuts import render
    from rest_framework import status
    from rest_framework.response import Response
    from rest_framework.views import APIView
    from .models import Post
    from .serializers import PostSerializer


    class PostList(APIView):
        def get(self, request):
            posts = Post.objects.all()
            serializer = PostSerializer(
                posts,
                many=True,
                context={'request': request}
            )
            return Response(serializer.data)
    ```

5. create a new `urls.py` file in the `posts` app
    - import:
        - `path` from `django.urls`
        - `views` from `posts` (`views.py` from the posts app)
    - create the `urlpatterns` list.
        - add a `path` for `'posts/'` that takes `Postlist` from `views` `as_view()`

    ```py
    from django.urls import path
    from posts import views

    urlpatterns = [
        path('posts/', views.PostList.as_view()),
    ]
    ```
6. in `drf_api/urls.py` `include` the `urls` from `posts`
    ```py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api-auth/', include('rest_framework.urls')),
        path('', include('profiles.urls')),
        path('', include('posts.urls')),
    ]
    ```
7. run the server, check the get request works so far (add /posts/ to the browser window url)

### Define the Post Method

> To actually have posts appear, we have to  make it possible for our users to create them. To achieve that, we have to define the post method inside the PostList view.

the `post` method needs to achieve the following:
1. deserialize request data
2. if the data is valid, save the post with the user as the owner
3. return the post with the 201 CREATED code
4. if the data is invalid, return the ERROR: 400 BAD REQUEST code

steps:
1. in the `PostList` class in `posts/views.py`, `def`ine the `post` method, passing it in the arguments of `self` and `request`:
2. inside the `post` method, create the `serializer` variable, its value being the `PostSerializer`, which will in-turn, handle the following parameters:
    - `data`, which will have the value of `data` from the `request`
    - `context`, which has a {K: V} Pair of K: `'request'` V: `request`
3. inside the function, below the `serializer`, write an `if` statement that checks if the `serializer` `is_valid()`
    - if it is, make the `serializer` `save()` the post, passing a parameter to `save()` that defines the `owner` of the post to be the `user` that made the `request`
    - then, close the `if` statement by `return`ing a `Response` that contains the `data` from `serializer` and a `status` that has a value of `HTTP_201_CREATED` from `status` codes
4. below the `if` statement, in lieu of an `else` statement, `return` a `Response` that takes any `errors` raised by `serializer` and pass a `status` of `HTTP_400_BAD_REQUEST` from `status`
5. > To have a nice create post form rendered in the preview window, let’s also set the serializer_class attribute to PostSerializer on our PostList class.
    - at the top of the class, add a variable called `serializer_class`, its value should be `PostSerializer`

```py
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer


class PostList(APIView):
    serializer_class = PostSerializer

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(
            posts,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

the Post List view has now been created, however, at this point, if an unauthenticated user tries to create a post, django will throw an error. 

this can be mitigated using the `permissions` framwork from rest

6. add `permissions` as an import from `rest_framework` at the top of `views.py`
7. at the top of the `PostList` class, below the `serializer_classes` variable, add the `permission_classes` list variable, giving it a single entry in the list of:
    - `permissions.IsAuthenticatedOrReadOnly`

```py
from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer


class PostList(APIView):
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(
            posts,
            many=True,
            context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

go back to the preview and check it all works.

____________________________________________

## The Post Detail view
##### https://youtu.be/4poMrjNqqf4