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
7. [creating the Post app, its base model and serializer](#setting-up-the-post-app-resources)
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
    - create the PostDetail view
    - retrieve a record by id
    - update a record by id
    - delete a record by id

-------------------------------
#### lesson 3.5: tests
11. [Writing Tests | Post List Tests](#writing-tests--post-list-tests)
    - Walkthrough: https://youtu.be/Vdga_GUb6q0
    - How tests work | lifecycle of a test
    - how to write tests
    - test examples | make sure users can:
        - list all posts
        - unauthenticated cant create posts
        - only authenticated users can create posts
12. [Post Detail tests](#post-detail-tests)
    - Walkthrough: https://youtu.be/Epg16CCQHlQ
    - test examples | make sure users can:
        - User can retrieve a post with a valid id
        - User can't retrieve a post with an invalid id (404)
        - Users can update the posts that they own

---------------------------------
#### lesson 4: Comments resource
13. [creating the Post app, its base model and serializer](#setting-up-the-post-app-resources)
    - Challenge, no video
    - Cretaing a new App
    - Creating the comments model
    - creating the comment serializer
14. [Creating a serializer that inherits from another](#creating-the-commentdetailserializer)
    - Challenge, no video
15. [Writing views using generics](#commentlist-and-commentdetail-generic-views)
    - Walkthrough: https://youtu.be/Xw6qDGQSbqs
    - how to write `CommentList` and `Detail` views using generics.
    - [docs: more info on generics](#more-info-on-generics)
    - [docs: more info on filtering](#more-info-on-filtering)

---------------------------------
#### lesson 5: likes resource
16. [creating the Like app, its base model and serializer](#creating-the-likes-app)
    - Challenge, no video
    - Creating a new App
    - Creating the Like model
    - creating the Like serializer
17. [Like Serializer Handling Duplicate Likes / Integrity Errors](#like-serializer-handling-duplicate-likes--integrity-errors)
    - Walkthrough: https://youtu.be/H1by3Yc2aYQ
    - handling Integrity Errors
        - caused by posible duplications
18. [Create the Likes views using Generic Views](#create-the-likes-views-using-generic-views)
    - Walkthrough: https://youtu.be/W4_vefxcVzg
    - create LikeList and LikeDetail views using generics
----------------------------------
#### Lesson 6: the Follower Resource
19. [Followers app and model build challenge](#creating-the-followers-app)
20. [Followers Serializer challenge](#creating-the-follower-serializer)
21. [Follower Views challenge](#creating-follower-app-views-using-generics)

-------------------------------------

#### lesson 6.5: refactoring profile and post apps
22. [Refactoring challenge](#refactoring-post-and-profile-views)

--------------------------------------

#### Lesson 7: Data Filtering
23. [Adding Extra Fields to Posts and Profiles Part 1](#adding-extra-fields-to-profiles-and-post-apps)
    - adding an extra field to the profile serializer to include whether or not a logged in user has followed another user.
    - adding an extra field to the post serializer to include whether or not a logged in user has liked a post.
24. [Adding Extra field to posts and Profiles Part 2](#adding-extra-fields-to-posts-and-profiles-part-2)
    - adding a number of posts a user has made to their profile
    - adding a count of the followers a user has
    - adding a count for the number of profiles a user is following
    - using the annotate function
    - make fields sortable with filters
25. [Adding Extra Fields to Post challenge](#adding-extra-fields-to-post-challenge)
    - challenge
26. [adding a search feature to the API](#adding-a-search-feature-to-the-api)
    Walkthrough: https://youtu.be/_GmXX51kvtY
    - create text search for Posts, search either by Author's username or port title
27. [Adding the filter feature to our API](#adding-the-filter-feature-to-our-api)
    - Walkthrough: https://youtu.be/Xx6JmpgN0qs
    - add a filter feature to filter the API data
        - posts owned by a user
        - posts liked by a user
        - posts by another user that a user us following
        - filter user list of accounts a user is following
    - using django_filters library

__________________________________________________________

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

this section covers:
- create the PostDetail view
- retrieve a record by id (get)
- update a record by id (put)
- delete a record by id (delete)

Post CRUD Table:
> Let’s have a look at our CRUD table. It shows what kind of HTTP request our users have to make and to which URL in order to list all posts, create, read, update or delete a post. 

| HTTP           | URI           | CRUD Operation                                                                   | View Name         |
| :------------: | :-----------: | :------------------------------------------------------------------------------: | :---------------: |
| **a**.GET / **b**.POST | /posts     | **a**.list all posts / **b**.create a post                         | LIST              |
| **c**.GET / **d**.PUT / **e**.DELETE | /posts/:id | **c**.retrieve a post by id / **d**.update a post by id / **e**.delete a post by id | DETAIL           |

### Create the PostDetail view
steps:
1. go to `posts/views.py`, start by importing the following:
    - `from django.Http import Http404`
    - the custom made permission `IsOwnerOrReadOnly` from `permissions.py` in `drf_api`
        - `from drf_api.permissions import IsOwnerOrReadOnly` 
2. create a new class called `PostDetail` that inherits from `APIView`
3. add the `permission_classes`, there should only be one in the list for now, the `IsOwnerOrReadOnly` permission
    - `permission_classes = [IsOwnerOrReadOnly]`
4. To format the edit form right out the gate, add the `serializer_class` too, which will be `PostSerializer`
    - `serializer_class = PostSerializer`

#### `get` request
5. write the `get_object` method for the view, it should take `self` and `pk` as arguments
    - add in a `try` statement which creates a variable called `post` which `get`s an `object` from `Post` that has a `pk` that matches the `pk` passed in as the argument for the method
        -`post = Post.objects.get(pk=pk)`
    - then, check the permissions of the post and if the accessing user has permission to edit it by using `check_object_permissions` on the instance(`this`), passing it the arguments of `self.request` and the `post` variable
        - `self.check_object_permissions(self.request, post)`
    - `return` the `post` variable
    - then, add an `except`ion for in the event that a `Post` `DoesNotExist`, in which case, the `Http404` error should be `raise`d
6. now, ceate the actual `get` method of the view, passing it `self`, `request` and `pk` as arguments
    - create a variable called `post` that uses the just-defined `get_object` method on the instance thats calling it (`self`) and pass it an argument containing the `pk`
    - beneath that, add a `serailizer` variable that takes the `PostSerializer` and runs the newly-defined `post` variable through it as a parameter, in addition to a `context` parameter with a {Key: Value}Pair of `'request': request`
    - `return` a `Response` containing the `data` from the `serializer`

    ```py
    from django.shortcuts import render
    from django.http import Http404
    from rest_framework import status, permissions
    from rest_framework.response import Response
    from rest_framework.views import APIView
    from .models import Post
    from .serializers import PostSerializer
    from drf_api.permissions import IsOwnerOrReadOnly

    ...

    class PostDetail(APIView):
        permission_classes = [
            IsOwnerOrReadOnly
        ]
        serializer_class = PostSerializer

        def get_object(self, pk):
            try:
                post = Post.objects.get(pk=pk)
                self.check_object_permissions(self.request, post)
                return post
            except Post.DoesNotExist:
                raise Http404
        
        def get(self, request, pk):
            post = self.get_object(pk)
            serializer = PostSerializer(
                post,
                context={'request': request}
            )
            return Response(serializer.data)
    ```

7. now, add the path for the new view in `posts/urls.py`:
    - in `urlpatterns` add a new `path` for `posts/<int:pk>`, where the `PostDetail` from views is rendered `as_` a `view()`

    ```py
    from django.urls import path
    from posts import views

    urlpatterns = [
        path('posts/', views.PostList.as_view()),
        path('posts/<int:pk>/', views.PostDetail.as_view()),
    ]
    ```

#### `put` request
more detailed explanation on how to do this in the [profile](#updating-an-existing-profile), **although be sure to add `context` to the `serializer` as it isn't done in that part of the tutorial yet**

8.  ```py
    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(
            post, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
    ```

#### `delete` request

9. in the class, `def`ine a `delete` method that takes `self`, `request` and `pk` as parameters
    - define the `post` variable and give it a value using the `get_object` method on the instance(`this`) by using the `pk`
        - `post = self.get_object(pk)`
    - run the `delete()` action on the `post` variable
        - `post.delete()`
    - `return` a `Response` containing a `status` parameter with the value of `HTTP_204_NO_CONTENT` from `status`
        - `return Response(status=status.HTTP_204_NO_CONTENT)`

    ```py
    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
    ```
10. check it all works

finished view code:

```py
from django.shortcuts import render
from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from drf_api.permissions import IsOwnerOrReadOnly

...

class PostDetail(APIView):
    permission_classes = [
        IsOwnerOrReadOnly
    ]
    serializer_class = PostSerializer

    def get_object(self, pk):
        try:
            post = Post.objects.get(pk=pk)
            self.check_object_permissions(self.request, post)
            return post
        except Post.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(
            post,
            context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(
            post, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )
    
    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
```

__________________________________________________________

## Writing Tests | Post List Tests
##### https://youtu.be/Vdga_GUb6q0

- how tests work | test lifecycle
- how to write tests
- test examples | make sure users can:
    - list all posts
    - unauthenticated cant create posts
    - only authenticated users can create posts

> In the next two videos, you’ll learn how to test both views using the red-green-refactor process, where we first make sure the test fails and then we write the code to make it pass.

### How tests work
> Let’s have a look at what happens when we run the test command. At the very beginning, before any test is run, the test database is created.  
> Then, before every test, the test database is flushed, which means that any data in it is destroyed.  
> Then, the setUp method runs, and finally the test. The cycle repeats for each test method.
> Eventually, at the very end, once all of the tests have been run, the test database is destroyed.

1. got to `posts/tests.py`
2. import the `User` and `Post` models:
    - `from django.contrib.auth.models import User`
    - `from .models import Post`
3. import `status` from `rest_framework`
4. import `APITestCase` from `rest_framework.test`
    -   ```py
        from django.contrib.auth.models import User
        from .models import Post
        from rest_framework import status
        from rest_framework.test import APITestCase
        ```
5. create a class called `PostListViewTests` that inherits from `APITestCase`
6. > First, we’ll define the setUp method that will automatically run before every test method in the class:
    - `def`ine a `setUp` method that takes `self` as a parameter
    - inside the method, `create_` a new `user` `object` in the `User` table, giving it the following parameters:
        - `username='adam'`
        - `password='pass'`
        - `User.objects.create_user(username='adam', password='pass')`
        - > We’ll use this user’s credentials when we need to log in to create a post. We’ll also need this user when we manually create a post and need to set its owner.
7. > Now, let’s test that we can list posts present in the database:
    - `def`ine a method called `test_can_list_posts` with `self` as an argument
    - define the test user in a variable called `adam` by setting its value to `User.objects.get(username='adam')`
    - `create` a new `Post` `object` with the following parameters:
        - `owner=adam`
        - `title='test post title`
        - it should look like: `Post.objects.create(owner=adam, title='a title')`
    - make a variable called `response`, its value should be:
        - `response = self.client.get('/posts/')`
        - > What I want to test now, is that I can make a  get request to ‘/posts’ to list all the posts. You make test network requests by calling an appropriate method on self-dot-client, namely self.client.get or .post, .put, and so on, followed by the url we’re making the request to.
    - start by testing that the test works by `assert`ing an incorrect `status` code of `HTTP_201_CREATED` (should be 200)
        - `self.assertEqual(response.status_code, status.HTTP_201_CREATED)`

    ```py
    from django.test import TestCase
    from django.contrib.auth.models import User
    from .models import Post
    from rest_framework import status
    from rest_framework.test import APITestCase


    class PostListViewTests(APITestCase):
        def setUp(self):
            User.objects.create_user(username='adam', password='pass')
        
        def test_can_list_posts(self):
            adam = User.objects.get(username='adam')
            Post.objects.create(owner=adam, title='a title')
            response = self.client.get('/posts/')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    ```
8. Run the test in the temrinal using the command:
    - `python3 manage.py test`
    - the following information should be returned in the terminal:
        ```
        Creating test database for alias 'default'...
        System check identified no issues (0 silenced).
        F
        ======================================================================
        FAIL: test_can_list_posts (posts.tests.PostListViewTests.test_can_list_posts)
        ----------------------------------------------------------------------
        Traceback (most recent call last):
        File "/workspace/django-REST-walkthrough/posts/tests.py", line 16, in test_can_list_posts
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        AssertionError: 200 != 201

        ----------------------------------------------------------------------
        Ran 1 test in 0.089s

        FAILED (failures=1)
        Destroying test database for alias 'default'...
        ```
9. > let's adjust it to `200_OK`, `print(response.data)` and its `length`. We’ll see the API is responding with a single post, the one we just created:
    - amended test:
        ```py
        def test_can_list_posts(self):
            adam = User.objects.get(username='adam')
            Post.objects.create(owner=adam, title='a title')
            response = self.client.get('/posts/')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            print(response.data)
            print(len(response.data))
        ```
    - running the test again, the terminal should return this:
        ```
        Creating test database for alias 'default'...
        System check identified no issues (0 silenced).
        [OrderedDict([('id', 1), ('owner', 'adam'), ('profile_id', 1), ('created_at', '2023-08-16T08:32:12.759797Z'), ('updated_at', '2023-08-16T08:32:12.759811Z'), ('title', 'a title'), ('content', ''), ('image', 'https://res.cloudinary.com/deth0ifla/image/upload/v1/media/../samples/landscapes/girl-urban-view'), ('image_filter', 'normal'), ('is_owner', False)])]
        1
        .
        ----------------------------------------------------------------------
        Ran 1 test in 0.083s

        OK
        Destroying test database for alias 'default'...
        ```

### only authenticated users can create posts
> Let’s now make sure that a logged in user can create a post. To test protected routes (which are routes  that require the user to be logged in), we’ll have to log in first using the APITest client.

1. `def`ine a new method called `test_logged_in_user_can_create_post` that takes a `self` argument
2. inside the new method, use the `self.client` method to `login`, using the username and password defined in the `setUp` method
3. create a `response` variable, its value should be a call to `self.client` to `post` an object to `/posts/`, the value of the post being a KVP of `{'title': 'a title'}`
4. create a `count` variable that `count()`s the amount of `objects` in the `Post` table
5. check to see if the number of posts `count`ed is equal to `1` by using the `assertEqual` method on the instance (`this`)
6. use the `assertEqual` method to also check the `response`'s `status_code` and make sure it matches `status.HTTP_200_OK`
    - this will force the test to fail due tot he status code not being correct.
    - to make is work, change the status code to `HTTP_201_CREATED`

test should look like:

    ```py
    def test_logged_in_user_can_create_post(self):  # 1
        self.client.login(username='adam', password='pass')  # 2
        response = self.client.post('/posts/', {'title': 'a title'})  # 3
        count = Post.objects.count()  # 4
        self.assertEqual(count, 1)  # 5
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # 6
    ```

and should return the following in the terminal:

    ```
    Creating test database for alias 'default'...
    System check identified no issues (0 silenced).
    1
    ..
    ----------------------------------------------------------------------
    Ran 2 tests in 0.248s

    OK
    Destroying test database for alias 'default'...
    ```

### Unauthentcated Users can't create posts

this test works the same as the one above, except it doesnt need to pass in a login, it just needs a `response` to check:

it goes through the exact same prcess, except it asserts that the statuscode from the response should be a 403, not a 201

    ```py
    def test_user_not_logged_in_cant_create_post(self):
            response = self.client.post('/posts/', {'title': 'a title'})
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    ```

_______________________________________________________________

## Post Detail Tests
##### https://youtu.be/Epg16CCQHlQ

- test examples | make sure users can:
    - User can retrieve a post with a valid id
    - User can't retrieve a post with an invalid id (404)
    - Users can update the posts that they own
    
### User can retrieve a post with a valid id

1. go to `posts/tests.py`
2. create a `PostDetailViewTests` class that inherits from the prreviously imported `APITestCase`
3. inside the new class, `def`ine a new `setUp` function with the argument of `self`
4. create 2 new users inside the function:
    - `adam`
    - `anna`
    - `<username> = User.object.create_user(username='<username>' password='<password>')`
5. then create a post owned by each user inside the function
    - `Post.objects.create(owner='<username>', title='<atitle>', content='<username>'s post')`

    ```py
    class PostDetailViewTests(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='pass1')
        anna = User.objects.create_user(username='anna', password='pass2')
        Post.objects.create(owner=adam, title='ADAM!', content="Adam's post")
        Post.objects.create(owner=anna, title='ANNA!', content="Anna's post")
    ```

6. with `setUp` now complete, `def` a new function in `PostDetailViewTests` called `test_can_retrieve_post_using_valid_id` with `self` as the argument
7. inside this function, `get` post `1` from `/posts/` in the instance (`this`) of the `client` and house it in a variable called `response`
8. then, `assert` wether the `response.data`'s `'title` is `Equal` to `'ADAM!'` 
9. then, use the same process to check if the `response.status_code` is correct (`status.HTTP_200_OK`)

    ```py
    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'ADAM!')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    ```

### User can't retrieve a post with an invalid id (404)

1. inside `PostDetailViewTests`, take the `test_can_retrieve_post_using_valid_id` function and copy/paste it underneath itself
2. amend its name to `test_cant_retrieve_post_using_invalid_id`
3. remove the line of code that checks the title of a post
4. in the `response`, change the post id in the `get` request from `1` to a ridiculous number
5. in the remaining `assertEqual` statement, change the expected status code to `HTTP_404_NOT_FOUND`

    ```py
    def test_cant_retrieve_post_using_invalid_id(self):
        response = self.client.get('/posts/999999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    ```

### Users can update the posts that they own

1. in the `PostDetailViewTests` class `def`ine function at the bottom of the class called `test_user_can_update_own_post`, pass it the `self` argument
2. make the instanced `client` `login` with `adam`'s credentials
3. create a `response` from the `client`, which should be a `put` request to `/posts/1/`, updating the posts title via way of `{'K':'V'}`P
4. create a `post` variable that `filter`s for the `Post` `object` that was just updated. append it with `.first()` so that it returns the first/only 1 result
5. `assertEqual` on `self` checking that the `title` of `post` is the same as the new title supplied in the `{'K':'V'}`P in step **3**.
6. then, use the same process to check if the `response.status_code` is correct (`status.HTTP_200_OK`)

    ```py
    def test_user_can_update_own_post(self):
        self.client.login(username='adam', password='pass1')
        response = self.client.put('/posts/1/', {'title': 'ADAAAAAM!'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'ADAAAAAM!')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    ```

7. conversely, make sure that users **can't** update posts that they **don't** own. copy the last function and amend its name to:
    - `test_user_cant_update_others_post`
8. in `response`, change the id the `put` request is trying to update from `1` to `2`
9. remove the lines of code for the `post` variable and the `assertEqual` command that checks the post title
10. update the remaining `assertEqual` to assert that the status code should be `status.HTTP_403_FORBIDDEN`

    ```py
    def test_user_cant_update_others_post(self):
        self.client.login(username='adam', password='pass1')
        response = self.client.put('/posts/2/', {'title': 'ADAAAAAM!'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    ```
    Finished Test code:
    ```py
    class PostDetailViewTests(APITestCase):
        def setUp(self):
            adam = User.objects.create_user(username='adam', password='pass1')
            anna = User.objects.create_user(username='anna', password='pass2')
            Post.objects.create(owner=adam, title='ADAM!', content="Adam's post")
            Post.objects.create(owner=anna, title='ANNA!', content="Anna's post")

        def test_can_retrieve_post_using_valid_id(self):
            response = self.client.get('/posts/1/')
            self.assertEqual(response.data['title'], 'ADAM!')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_cant_retrieve_post_using_invalid_id(self):
            response = self.client.get('/posts/999999/')
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
        def test_user_can_update_own_post(self):
            self.client.login(username='adam', password='pass1')
            response = self.client.put('/posts/1/', {'title': 'ADAAAAAM!'})
            post = Post.objects.filter(pk=1).first()
            self.assertEqual(post.title, 'ADAAAAAM!')
            self.assertEqual(response.status_code, status.HTTP_200_OK)

        def test_user_cant_update_others_post(self):
            self.client.login(username='adam', password='pass1')
            response = self.client.put('/posts/2/', {'title': 'ADAAAAAM!'})
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    ```
___________________________________________________________________________

## Setting up the Comments App resources
##### [challenge page](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/601b5665c57540519a2335bfbcb46d93/10d957d204794dbf9a4410792a58f8eb/?child=first)

1. run the command in the terminal to make a new app, name it `comments`
    - `python3 manage.py startapp comments`
2. add it to `INSTALLED_APPS` in settings.py

### Creating a comments model
1. in `comments/models.py` import the following:
    - `models` from `django.db`
    - `User` from `django.contrib.auth.models`
    - `Post` from `posts.models`
    ```py
    from django.db import models
    from django.contrib.auth.models import User
    from posts.models import Post
    ```

2. create a class called `Comment`, it should inherit from `models.Model`
3. the new `Comment` class needs the following fields:
    - owner, which should be a `ForeignKey` using the `User` as its value, it should also `CASCADE` delete any related sub-items if deleted
    - post, which should be a `ForeignKey` using the `Post` as its value, it should also `CASCADE` delete any related sub-items if deleted
    - created_at, which should be a `DateTimeField` which should be automatically assigned a new value upon record creation by using the parameter `auto_now_add=True`
    - updated_at, same as above, except its paramater is `auto_now=True`, not `auto_add_now` as it updates every time the post is edited, not when it is `add`ed
    - content, should be a `TextField` to house post content
   
4. add a `Meta` class that orders posts by the `DateTime` they were `created_at`, with the most recent entry being first
5. define a dunder `str` method that returns the `content` of `self`

the post model should look like this:
```py
from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    """
    Comment model, related to User and Post
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
```

6. Migrate the completed model into the database
    1. `python3 manage.py makemigrations`
    2. `python3 manage.py migrate`


### creating the comment serializer

1. create a new file in `comments` called `serializers.py`
2. inside the new `serailizers` import:
    - `serializers` from `rest_framework`
    - the `Comment` model from `.models`
3. create a class called `CommentSerializer` which inherits from `serializers.ModelSerializer`
4. establish the following serailizer fields:
    - owner: a `ReadOnlyField` that's `source` is the `username` of the `owner` specified in the `Comment` model
    - profile_id: a `ReadOnlyField` that's `source` is the `id` of the `owner` specified in the `Comment` model (`id`'s are automatically created by django)
    - profile_image: a `ReadOnlyField` that's `source` is the `url` of the `image` field beonging to the `owner`, specified in the `Comment` model
    - is_owner: a variable which houses the `SerializerMethodField` for the `serializer`
5. use the `is_owner` field to create a method (prefix it with `get_`) with the following parameters: `self` and `obj` for object in question
    - the function should then take a `context`ual `request` from whatever calls it (`this`), and then checks if the `user` that made the `request` matches the `obj`'s `owner`, `return`ing a boolean value depending on the outcome
6. add a `Meta` class that:
    - determines the `model` the serializer its basing its structure from, n this case it is `Comment`
    - determine the `fields` it serializes and displays in a list variable as strings, they should be:
        - id
        - owner
        - profile_id
        - profile_image
        - post
        - created_at
        - updated_at
        - content
        - is_owner

finished serializer shuold look like this:
```py
from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
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
        model = Comment
        fields = [
            'id',
            'owner',
            'profile_id',
            'profile_image',
            'created_at',
            'updated_at',
            'post',
            'content',
            'is_owner',
        ]
```

___________________________________________________________

## Creating the CommentDetailSerializer
#### Creating a Serializer that inherits from another

1. in `comments/serializers.py`, create a new class called `CommentDetailSerializer`. make it inherit from the previously created `CommentSerializer` class
2. give it a variable of `post`: a `ReadOnlyField` that's `source` is the `id` of the `post` specified in the `Comment` model

```py
class CommentDetailSerializer(CommentSerializer):
    post = serializers.ReadOnlyField(source='post.id')
```
> Because CommentDetailSerializer inherits from CommentSerializer, all its methods and attributes are already included e.g. Meta.

___________________________________________________________

## CommentList and CommentDetail generic views
##### https://youtu.be/Xw6qDGQSbqs
##### [more info on Generics](https://www.django-rest-framework.org/api-guide/generic-views/#attributes/)
##### [more info on filtering](https://www.django-rest-framework.org/api-guide/filtering/)

how to write `CommentList` and `Detail` views using generics.

> The Django Documentation states that generic views were developed as a shortcut for common usage patterns. What this means is that we can achieve  all the same functionality of the get, post, put and other class based view methods without having to repeat ourselves so much.

steps:
1. go to `views.py` in the `comments` app. 
2. import the following:
    - `generics` from `rest_framework`
    - `IsOwnerOrReadOnly` from `permissions` in `drf_api`
    - `Comment` from `.models`
    - `CommentSerializer` and `CommentDetailSerializer` from `.serializers`

#### Create the CommentList View

3. create a class called `CommentList` that inherits from `generics.ListCreateAPIView`
    - > As we want to both [list] and [create] comments in the ListView, instead of explicitly defining the post and get methods like we did before, I’ll extend generics’ [List][Create]APIView. Extending the [List]APIView means we won’t have to write the get method and the [Create]APIView takes care of the post method.
    - **list** covers the get request
    - **create** covers the post request
4. set the `serailizer_class` to `CommentSerializer`
5. set the `permission_classes` to `[permissions.IsAuthenticatedOrReadOnly]`
6. Add a queryset variable that `get`s `all()` the `objects` in the `Comment` table
    - > Instead of specifying only the model we’d like  to use, in DRF we set the queryset attribute. This way, it is possible to filter  out some of the model instances. This would make sense if we were  dealing with user sensitive data like orders or payments where we would need to  make sure users can access and query only their own data. In this case however, we want all the  comments.
    - [**Learn more about attribute and data filtering here**](https://www.django-rest-framework.org/api-guide/filtering/)

code so far:

    ```py
    from rest_framework import generics, permissions
    from drf_api.permissions import IsOwnerOrReadOnly
    from .models import Comment
    from .serializers import CommentSerializer, CommentDetailSerializer

    class CommentList(generics.ListCreateAPIView):  # step 3
        serializer_class = CommentSerializer  # step 4
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # step 5
        queryset = Comment.objects.all()  # step 6
    ```
> Before we test the view, we’ll have to make sure comments are associated with a user upon creation. We do this with generics by defining the perform_create method

7. `def`ine a method called `perform_create` which takes the arguments of `self` and `serializer`
    - > the `perform_create` method takes in `self` and `serializer` as arguments. Inside, we pass in the user making the request as owner into the serializer’s save method, just like we did in the regular class based views.
8. call the `save()` command on the `serializer`, in the argument of `save` define the `owner` as the `user` making the `request`
    - views using generics:
        ```py 
        from rest_framework import generics, permissions
        from drf_api.permissions import IsOwnerOrReadOnly
        from .models import Comment
        from .serializers import CommentSerializer, CommentDetailSerializer

        class CommentList(generics.ListCreateAPIView):  # step 3
            serializer_class = CommentSerializer  # step 4
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # step 5
            queryset = Comment.objects.all()  # step 6

            def perform_create(self, serializer):  # step 7
                serializer.save(owner=self.request.user)  #step 8
        ```
    - views manually written equivalent:
        ```py
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

    > More good news is that with generics, the request  is a part of the context object by default. What this means is that we no longer have to pass it manually,  like we did in the regular class based views.

9. now, create the `urls` for the comments. create the `urls.py` file in the `comments app`
10. import the following into `comments/urls.py`:
    - `from django.urls import path`
    - `from comments import views`
11. next, create the `urlpatterns` list beneath the imports, it should contain the following paths:
    - `'comments/'` which should take the `CommentList` `view` and render it `as_view()`

```py
urlpatterns = [
    path('comments/', views.CommentList.as_view()),
]
```

12. then, in `drf_api/views` add the `'comments.urls'` to a `path` by using the `include` method
    ```py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api-auth/', include('rest_framework.urls')),
        path('', include('profiles.urls')),
        path('', include('posts.urls')),
        path('', include('comments.urls')),  # step 12
    ]
    ```

#### create the CommentDetail view

13. create a class called `CommentDetail` and have it inherit from `generics.RetrieveUpdateDestroyAPIView`
    - from generics, the following methods are pulled in the inherited model name to automatically streamline the coding for the following types of requests:
        - `Retrieve` data
        - `Update` data
        - `Destroy` data
        - jump back up [here](#create-the-commentlist-view) for a fuller explanataion
        - [documentation on generics](https://www.django-rest-framework.org/api-guide/generic-views/#attributes/)
14. set the `permission_classes` list of the new class to the imported `[IsOwnerOrReadOnly]` permission
15. set the `serializer_class` for the class to `CommentDetailSerializer`
    - > Our serializer still needs to access the request, but as mentioned before, we don’t really need to do anything, as the request is passed in as part of the context object by default.
16. define the `queryset` for the class, querying `all()` the `objects` in the `Comment` table

```py
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):  # step 13
    permission_classes = [IsOwnerOrReadOnly]  # step 14
    serializer_class = CommentDetailSerializer  # step 15
    queryset = Comment.objects.all()  # step 16
```

17. with the class created, head back to `comments/urls.py` and add a new path to the `urlpatterns` list, this time it should be for `comments/<int:pk>/`, (<int:pk>: the primary key is being told to be handled as an integeter). It should render the `CommentDetail` `view` `as_view()`

```py
urlpatterns = [
    path('comments/', views.CommentList.as_view()),
    path('comments/<int:pk>', views.CommentDetail.as_view()),  # step 17
]
```
_______________________________________________________________________
## setting up the like app
##### [challenge page](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/601b5665c57540519a2335bfbcb46d93/241dbe57cd2a466dba5f7d37f67e2cb8/?child=first)
##### Challenge, no video

- Creating a new App
- Creating the Like model
- creating the Like serializer


### Creating the Likes app

1. run the command in the terminal to make a new app, name it `likes`
    - `python3 manage.py startapp likes`
2. add it to `INSTALLED_APPS` in settings.py


### Creating the Like Model

3. go to `likes/models.py`
4. add all of the following imports:
    ```py
    from django.db import models
    from django.db.models import UniqueConstraint
    from django.contrib.auth.models import User
    from posts.models import Post
    from comments.models import Comment
    ```
5. create the `Like` class, that inherits from `models.model`
6. add the following fields to the new class to create the data model:
    - owner: should be a ForeignKey linked to the `User` table, with an `on_delete` property of CASCADE
    - post: should be a ForeignKey with a [`related_name`](https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.ForeignKey.related_name) of `likes`, with an `on_delete` property of CASCADE
    - created_at: a DateTimeField which has a paroperty of `auto_now_add=True`
7. assign the `Like` class a `Meta` class which:
    - reverse orders items in the table based on the time they were created
    - ~~add a [`unique_together`](https://docs.djangoproject.com/en/3.2/ref/models/options/#unique-together) field between owner and post~~
        - `unique_together` will be deprecated in the future, django docs advise the use of `constraints = [UniqueConstraint()]` instead
        - add a constraints variable that takes a list value containing a `UniqueConstraint` that links the `owner` and `post` to each individual like, making them unique
            - [link to documentation on how to use constraints](https://docs.djangoproject.com/en/3.2/ref/models/constraints/)
        > With things like UniqueConstraint, it's not actually making particular changes to the model itself. The code you've written will check the request before it tries to alter the database....so in this case, check if the owner and post ID's are already present together.
        > Metaclasses are used to provide things like validation, without needing to alter the actual model itself. Generally, it'll be things like setting the name, ordering, unique constraints etc.
8. add a dunder `str` method to the end of the class that `return`s a string containing the `owner` and `post` fields


### Creating the Like serializer

1. create a new file in `likes` called `serializers.py`
2. inside the new `serailizers` import:
    - `serializers` from `rest_framework`
    - the `Like` model from `.models`
3. create a class called `LikeSerializer` which inherits from `serializers.ModelSerializer`
4. establish the following serailizer fields:
    - owner: a `ReadOnlyField` that's `source` is the `username` of the `owner` specified in the `Post` model
5. add a `Meta` class that:
    - determines the `model` the serializer its basing its structure from, in this case it is `Like`
    - determines the `fields` it serializes and displays in a list variable as strings, they should be:
        - id
        - owner
        - created_at
        - updated_at

________________________________________________________________________

## Like Serializer Handling Duplicate Likes / Integrity Errors
##### https://youtu.be/H1by3Yc2aYQ

> In this video, we will learn how to prevent  our users from liking the same post twice.

Because the `Like` model has a `Meta` class that prevents duplicate likes from a single user on a single post, trying like a post more than once will cause an **Integrity Error**. to avoid this, update the serializer with a method that can handle the error in an exception using a `try`/`except` statement. 

1. first, navigate to `serializers.py` in the `likes` app. at the top of the file, import:
    - `from django.db import IntegrityError`

1. then, Inside the `LikeSerializer` class, after its `Meta` class:
    - `def`ine a new `create` method that takes the arguments of `self` and `validated_data`
    - > Handling duplicates  with the rest framework is pretty easy. All we have to do is define the create method inside our LikeSerializer to return a complete object instance  based on the validated data.
2. add a `try` statement that tries to `return` the following:
    - `super().create(validated_data)`
        - > This create method is on the model serializer and for that reason I had to call “super()”.
3. then add an `except`ion on an `IntegrityError` that:
    - `raise`s a `ValidationError` from `serializers`, for its paramters, add a {K: V}P of `'detail'`: `'possible duplicate'`

```py
from django.db import IntegrityError
from rest_framework import serializers
from .models import Like


class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = [
            'id',
            'owner',
            'created_at',
            'post',
        ]

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
```
___________________________

## Create the Likes views using Generic Views
##### https://youtu.be/W4_vefxcVzg

> In this video, we will get more practice with generics by creating LikeList and LikeDetail generic views.

steps:
1. go to `views.py` in the `likes` app. 
2. import the following:
    - `generics` from `rest_framework`
    - `IsOwnerOrReadOnly` from `permissions` in `drf_api`
    - `Like` from `.models`
    - `LikeSerializer` from `.serializers`

#### Create the CommentList View

3. create a class called `LikeList` that inherits from `generics.ListCreateAPIView`
    - > As we want to both [list] and [create] comments in the ListView, instead of explicitly defining the post and get methods like we did before, I’ll extend generics’ [List][Create]APIView. Extending the [List]APIView means we won’t have to write the get method and the [Create]APIView takes care of the post method.
    - **list** covers the get request
    - **create** covers the post request
4. set the `serailizer_class` to `LikeSerializer`
5. set the `permission_classes` to `[permissions.IsAuthenticatedOrReadOnly]`
6. Add a queryset variable that `get`s `all()` the `objects` in the `Like` table
    - > Instead of specifying only the model we’d like  to use, in DRF we set the queryset attribute. This way, it is possible to filter  out some of the model instances. This would make sense if we were  dealing with user sensitive data like orders or payments where we would need to  make sure users can access and query only their own data. In this case however, we want all the  comments.
    - [**Learn more about attribute and data filtering here**](https://www.django-rest-framework.org/api-guide/filtering/)

code so far:

    ```py
    from django.shortcuts import render
    from rest_framework import generics, permissions
    from drf_api.permissions import IsOwnerOrReadOnly
    from .models import Like
    from .serializers import LikeSerializer


    class LikeList(generics.ListCreateAPIView):
        serializer_class = LikeSerializer
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        queryset = Like.objects.all()
    ```
> Before we test the view, we’ll have to make sure comments are associated with a user upon creation. We do this with generics by defining the perform_create method

7. `def`ine a method called `perform_create` which takes the arguments of `self` and `serializer`
    - > the `perform_create` method takes in `self` and `serializer` as arguments. Inside, we pass in the user making the request as owner into the serializer’s save method, just like we did in the regular class based views.
8. call the `save()` command on the `serializer`, in the argument of `save` define the `owner` as the `user` making the `request`
    - views using generics:
        ```py 
        from django.shortcuts import render
        from rest_framework import generics, permissions
        from drf_api.permissions import IsOwnerOrReadOnly
        from .models import Like
        from .serializers import LikeSerializer


        class LikeList(generics.ListCreateAPIView):
            serializer_class = LikeSerializer
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
            queryset = Like.objects.all()

            def perform_create(self, serializer):
                    serializer.save(owner=self.request.user)
        ```

    - views manually written equivalent:
        ```py
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

    > More good news is that with generics, the request is a part of the context object by default. What this means is that we no longer have to pass it manually,  like we did in the regular class based views.

9. now, create the `urls` for the comments. create the `urls.py` file in the `likes` app
10. import the following into `likes/urls.py`:
    - `from django.urls import path`
    - `from likes import views`
11. next, create the `urlpatterns` list beneath the imports, it should contain the following paths:
    - `'likes/'` which should take the `LikeList` `view` and render it `as_view()`

```py
urlpatterns = [
    path('likes/', views.LikeList.as_view()),
]
```

12. then, in `drf_api/views` add the `'likes.urls'` to a `path` by using the `include` method
    ```py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('api-auth/', include('rest_framework.urls')),
        path('', include('profiles.urls')),
        path('', include('posts.urls')),
        path('', include('comments.urls')),  # step 12
        path('', include('likes.urls')),  # step 12
    ]
    ```

#### create the LikeDetail view

13. in `likes/views.py` create a class called `LikeDetail` and have it inherit from `generics.RetrieveDestroyAPIView`
    - from generics, the following methods are pulled in the inherited model name to automatically streamline the coding for the following types of requests:
        - `Retrieve` data
        - `Destroy` data
        - > There’s no need to implement like updates, as our users will create a like when clicking the like button and destroy a like when clicking the button again.
        - jump back up [here](#create-the-commentlist-view) for a fuller explanataion
        - [documentation on generics](https://www.django-rest-framework.org/api-guide/generic-views/#attributes/)
14. set the `permission_classes` list of the new class to the imported `[IsOwnerOrReadOnly]` permission
    - > which will allow only the user who liked a post  to un-like it
    - [review it here](#creating-a-custom-permission)
15. set the `serializer_class` for the class to `LikeSerializer`
    - > Our serializer still needs to access the request, but as mentioned before, we don’t really need to do anything, as the request is passed in as part of the context object by default.
16. define the `queryset` for the class, querying `all()` the `objects` in the `Like` table

```py
class LikeDetail(generics.RetrieveDestroyAPIView):  # step 13
    permission_classes = [IsOwnerOrReadOnly]  # step 14
    serializer_class = LikeSerializer  # step 15
    queryset = Like.objects.all()  # step 16
```

17. with the class created, head back to `likes/urls.py` and add a new path to the `urlpatterns` list, this time it should be for `likes/<int:pk>/`, (<int:pk>: the primary key is being told to be handled as an integeter). It should render the `LikeDetail` `view` `as_view()`

```py
urlpatterns = [
    path('likes/', views.LiketList.as_view()),
    path('likes/<int:pk>/', views.LikeDetail.as_view()),  # step 17
]
```

_____________________________________________________________________

## Creating the Followers app
##### Challenge: https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/601b5665c57540519a2335bfbcb46d93/d29d4cc768c944b1b6127f429bc14c97/?child=first

1. create the app using the same methods used to create the other apps

2. create the `Follower` model with the follwoing spec:

Product Spec
- owner: ForeignKey
- set on_delete to cascade
- set related_name to 'following'
- followed: ForeignKey
- set on_delete to cascade
- set related_name to 'followed'
- created_at: DateTimeField
- add auto_now_add as True

Additionally:

- Create the Meta class:
    - add ordering field using reverse created_at.
    - Add unique_together field between owner and followed
- Create the __str__ dunder method:
    - return a string containing the owner and followed fields


```py
from django.db import models
from django.db.models import UniqueConstraint
from django.contrib.auth.models import User
from profiles.models import Profile

# Create your models here.

class Follower(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followed')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        constraints = [UniqueConstraint(fields=['owner', 'followed'], name='unique_follow')]

    def __str__(self):
        return f"{self.owner} {self.followed}"
```



##### [solution](https://github.com/Code-Institute-Solutions/drf-api/tree/1fff0efe7e9f9abcc0ea1ccea534742458e5dc01)

____________________________________________________________________

## Creating the Follower serializer 
##### challenge: https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/601b5665c57540519a2335bfbcb46d93/d29d4cc768c944b1b6127f429bc14c97/?child=first

all steps can be completed using previous lessons

Project Description
In the last challenge, we created our Follower Model. In this section, you will create the FollowerSerializer.

Important: Please ensure that your models are correct, and that you have migrated your models to the database. Use the following Followers Model Code to check, if you haven't done so already.

1. Serializer Spec
Now, your challenge is to create the FollowerSerializer, here’s the spec:

Product Spec
- owner: read only field
- followed_name: read only field

Additionally:
- Add the Meta class
- Add a 'create' function to handle duplication errors

2. Steps
Important: As previously mentioned, it is highly recommended to refer to a previous example of a serializer, as there will be less helpful hints in this challenge than the previous 'like serializer' challenge

1. 'followers' app
Create the followers/serializers.py file. Add the relevant imports (x3).
2. FollowerSerializer class
Use the spec document above to create the FollowerSerializer class including the owner, and followed_name fields, and meta class.
Add a create function to handle Integrity Errors.

```py
from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = [
            'id',
            'owner',
            'followed_name',
            'followed',
            'created_at',
        ]
    
    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
```

solution code:
https://github.com/Code-Institute-Solutions/drf-api/tree/5c6997afa15b3fc83bbfb5e7521fdb5711a021e5

_________________________________________________________

## Creating Follower app views using generics
##### Challenge: https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/601b5665c57540519a2335bfbcb46d93/d29d4cc768c944b1b6127f429bc14c97/?child=first

Generic Views Spec
Now, your challenge is to create the FollowerList generic view, here’s the spec:

Product Spec
- FollowerList: call upon the subclass to GET and POST
- set the serializer_class to FollowerSerializer
- set the queryset to all followers
- set the permission class to IsAuthenticateOrReadOnly


Additionally:
- Add the perform_create function.
- FollowerDetail: call upon the subclass to RETRIEVE and DELETE
- set the serializer_class to FollowerSerializer
- set the queryset to all followers
- set the permission class to IsOwnerOrReadOnly

Steps
Important: As previously mentioned, it is highly recommended to refer to a previous example of a generics view, such as 'likes / views.py'.

1. FollowerList
    - Add the appropriate imports (x4).
    - Pass the appropriate generics views into your class so that you can GET and POST your views.
    - Create the appropriate attributes based on the Product Spec above
    - Add the perform_create function (refer to likes/views.py)

2. FollowerDetail class
    - Pass the appropriate generics views into your class so that you can Retrieve and Delete your views.
    - Create the appropriate attributes based on the Product Spec above
3. URLs
    - Add your urls to the appropriate files.

```py
from django.shortcuts import render
from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    serializer_class = FollowerSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
```

Solution Code: https://github.com/Code-Institute-Solutions/drf-api/tree/a52eb3634a052033c8bf575a48b3d588c28da8a6
_________________________________________________________________________

## Refactoring Post and Profile views
##### https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/601b5665c57540519a2335bfbcb46d93/d29d4cc768c944b1b6127f429bc14c97/?child=first

1. Steps
Important: As you have already completed the Follower Generics View, we recommend that you spend some time to refactor at least one of either Profile or Post Views to using generics. You can then either continue to refactor the second app or use the links below to copy and paste.

Both Profile and Post need to be refactored before you continue on with the next unit.

1. Profile Generics View
Refactor your Profiles views to use Generic Views or copy and paste using the link provided:
[Profile Views Refactor Source Code](https://github.com/Code-Institute-Solutions/drf-api/blob/23b93337ab45903140ea01232474e9fbcad4f015/profiles/views.py)

2. Post Generics View
Refactor your Post views to use Generic Views or copy and paste using the link provided:
[Post Views Refactor Source Code](https://github.com/Code-Institute-Solutions/drf-api/blob/23b93337ab45903140ea01232474e9fbcad4f015/posts/views.py)

Make sure you test your code is working before continuing

______________________________________________________

## Adding extra Fields to Profiles and Post Apps
##### https://youtu.be/H3vYRGaq_4I

- adding an extra field to the profile serializer to include wether or not a logged in user has followed another user. 
    - basically, whenever a user follows another user, the Follower table updates with a record with a value of 
        - the owner (the person who made the follow)
        - and the followed (the profile the user followed.)
  any time a follow is made by any user, a new record is created with these values. These values are regulated as unique by the serializer from the previous lessons.
  this lesson updates the `ProfileSerializer` to - when an authenticated user logs in - filter through the `Follower` table and return records that are owned by that user, as this is an iterative process, it will do it for every record in the Table, meaning that is a list is generated, it will return a value for each record. 
  In this instance, the serializer will return the id of the follow. 
  the serializer will also use an `if` statement to check that a user is authenticated, if they are not, the filter for follows will not run, restulting in returning a `null` value for each record. 


1. go to `profiles/serializers.py/ProfileSerializer` and import the `Follower` model
    - `from followers.models import Follower`
2. then, inside the `ProfileSerializer` add a new variable called `following_id`. it should have the same value as `is_owner`, the variable above it, so that it creates a new field in the serializer.
3. `def`ine a new method called `get_following_id`, which calls the `get_` prefi on the new SerializerMethodField just created. ([more about the `get_` prefix here](#adding-custom-fields-depending-on-the-authentication-of-the-user-using-a-serializer)).
    - pass it arguments of `self` and `obj`
4. inside the new method, create a variable called `user`, its value should be the `user` from the `['request']` of the `context` of the `self` argument that had been passed in as an argument. 
    - `user = self.context['request'].user`
    - > Inside, I’ll get the current user from the context object and check if the user is authenticated.
5. add a conditional stateent to the function that, `if` the `user` `.is_authenticated`:
    - > Then I will check if the logged in user is following any of the other profiles.  
    - create a variable called `following`, assign it the value of the `objects` of the `Follower` table `filter`ed by: 
        - `owner`, where the value is the authenticated `user`
        - `followed`, where the value is the `owner` of the `obj` parameter passed in at the top of the function 
    - append the value with `.first()` so that it will only return the one value any time it runs.
6. add a print statement into the function to check its working correctly
7. then, at the end of the `if` statement, `return` the `id` of the newly established `following` variable from inside the `if` statement, appending an additional `if` statement onto it in the `return` statement to double check if following is `truthy` (has a value), else the statement will `return`` the value of `None`
    - `return following.id if following else None`
8. in lieu of an `else` statement on the outer `if` statement, provide a `return` statement that returns `None` in the event that the user is not authenticated


Finished code:
```py
from rest_framework import serializers
from .models import Profile
from followers.models import Follower

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        passes the request of a user into the serializer
        from views.py
        to check if the user is the owner of a record
        """
        request = self.context['request']
        return request.user == obj.owner

    # new function
    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, following=obj.owner
            ).first()
            # print(follwing)
            return following.id if following else None
        return None

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
            'is_owner',
            'following_id',  # new field
        ]
```

### adding the like_id field onto Posts with PostSerializer

as this theoretically works the exact same way is follows does with profiles, copy the steps above to achieve the same outcome for posts and likes:

ed result code following above method:

```py 
class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_id = serializers.ReadOnlyField(source='owner.id')
    profile_image = serializers.ReadOnlyField(source='owner.image.url')
    is_owner = serializers.SerializerMethodField()
        # this variable above is used to house 
        # the requisite serializer it is called 
        # as a function below by prefixing the variable's 
        # name with 'get_'
    like_id = serializers.SerializerMethodField()
        # newly added variable to run the serializer
        # to get an id of a like associated with the post 
        # and the authenticated user

    
    def get_is_owner(self, obj):
        """
        passes the request of a user into the serializer
        from views.py
        to check if the user is the owner of a record
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        # the like_id variable is prefixed with get_ to run
        # a specific method type
        user = self.context['request'].user
        # the user variable gets the user that 
        # prompted the method to run
        if user.is_authenticated:
            # checks if the user is authenticated 
            # if they are:
            liked = Like.objects.filter(owner=user, post=obj).first()
                # the liked variable runs on each entry in Post
                # and checks is a user is the owner of a like for that post
            print(liked)
                # just a print statement to check its all kushty in the CLI
            return liked.id if liked else None
                # for each entry, the serializer will return the id of the like
                # created for that post by that authenticated user
                # if the user hasnt made one, the method will return a "None" value
        return None
            # skip to end if user isnt authenticated and return "None" for all Posts
    
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
            'like_id',  # and don't forget to add the field!
        ]

```

_______________________________________________________________________

## Adding Extra fields to Posts and Profiles part 2
##### https://youtu.be/Eoi411is464

- adding a number of posts a user has made to their profile
- adding a count of the followers a user has
- adding a count for the number of profiles a user is following
- using the annotate function
- make fields sortable with filters


1. got to `views.py` in the `profiles` app

### adding a number of posts a user has made to their profile

2. make a new import at the top of the file:
    - `from django.db.models import Count`
3. add `filters` to imports from `rest_framework`
    - `from rest_framework import generics, filters`
4. in the `ProfileList` class, amend the `queryset` variable - instead of using `.all()` on the `Profile.objects`, use `.annotate()` function
    - > The annotate function allows  us to define extra fields to be added to the queryset. In our case, we’ll add fields to work  out how many posts and followers a user has, and how many other users they’re following.
    - inside the `annotate` function, pass in the following:
        - `posts_count` which will be equal to the `Count()` class imported in step 2
            - > what we’re trying to achieve here is to count the number of posts associated with a specific Profile. 
            
              > however, there is no direct relationship between Profile and Post. So we need to go through the User model to get there. 
              
              > So, inside the Count class, we will need to perform a lookup that spans the profile, user, and post models, so we can get to the Post model with the instances we want to count.
            - `posts_count=Count('owner__post', distinct=True)`
              > Similar to when we used dot notation, the first part of our lookup string is the owner field on the Profile model,  which is a OneToOne field referencing User. From there we can reach the  Post model. So we have to add ‘double underscore post’ to show the relationship between Profile, User and Post.

              >  we also need to pass distinct=True here to only count the unique posts. Without this we would get duplicates.
            - [more info on double underscore method and `distinct`](https://docs.djangoproject.com/en/3.2/topics/db/queries/#lookups-that-span-relationships)
    
    ```py
    class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
    )

    ```

### adding a count of the followers a user has

5. inside the queryset, beneath the `posts_count` parameter, add a `followers_count` parameter that also uses the `Count()` method
    - > This time we have a problem. Within the Follower model, we have two foreign keys that are referencing the User model. One to identify the User following another user and the other to identify the one being followed. 

      > So here, we need to use the related_names “following” and “followed” defined in followers’  models.py file, instead of the model name like we did for owner__post. The  string value then, will be ‘owner__followed’.  
    - inside the `Count()` method of `followers_count`, use the double underscore notation (`__`) on owner to connect to the `followed` field of the `Follower` model by its related name of `followed` (this may be the same as the variable name, but remember, this is the value its using to connect the fields, NOT the variable name)
        - `followers_count=Count('owner__followed', distinct=True),`
    

    ```py
    class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
    )

    ```

### adding a count for the number of profiles a user is following

6. repeat step 5 for the to count the amount of profiles a user is `following`, it should work the exact same way as `followers_count` as the `following` variable in the `Follower` model has a related name of `following`
7. with all 3 paramters added, `order` the `queryset` values `by` they date they were `created_at` in reverse. 

    ```py
    class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')

    ```

### make fields sortable with filters

8. after the `queryset` variable, set a new variable called `filter_backends`, which contains a list value with one entry of `filters.OrderingFilter` (taken from the `filters` import)
    - `filter_backends = [filters.OrderingFilter]`

9. now, after that, create another variable called `ordering_fields` which contains a list of the fields counted in the `annotate` method of the `queryset` above
    - `ordering_fields = ['posts_count', 'followed_count', 'following_count']`
10. > I’d also like to be able to sort our profiles by how recently they followed a profile and by how recently they have been followed by a profile.
    - in the `ordering_fields` list, add the `owner__followers` and `owner__following` like in the count methods, except this time, append them with `created_at` with `__`
    -   ```py
        class ProfileList(generics.ListAPIView):
            """
            List all profiles.
            No create view as profile creation is handled by django signals.
            """
            serializer_class = ProfileSerializer
            queryset = Profile.objects.annotate(
                posts_count=Count('owner__post', distinct=True),
                followers_count=Count('owner__followed', distinct=True),
                following_count=Count('owner__following', distinct=True),
            ).order_by('-created_at')
            ordering_fields = [
                'post_count',
                'followed_count',
                'following_count',
                'owner__followed__created_at',
                'owner__following__created_at'
            ]
        ```
    > As these are regular database fields, I don’t need to add them to the queryset, but I still have to add them to the ordering_fields list.
11. to make sure these new ordering/ordered fields can be viewed, they need to be passed into the serializer:

```py
from rest_framework import serializers
from .models import Profile
from followers.models import Follower

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    following_id = serializers.SerializerMethodField()
    posts_count = serializers.ReadOnlyField()
    followers_count = serializers.ReadOnlyField()
    following_count = serializers.ReadOnlyField()


    def get_is_owner(self, obj):
        """
        passes the request of a user into the serializer
        from views.py
        to check if the user is the owner of a record
        """
        request = self.context['request']
        return request.user == obj.owner

    def get_following_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            following = Follower.objects.filter(
                owner=user, followed=obj.owner
            ).first()
            print(following)
            return following.id if following else None
        return None

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
            'is_owner',
            'following_id',
            'posts_count',
            'followed_count',
            'following_count',
        ]
```
____________________________________________________________

## Adding extra Fields to post challenge
##### [challenge](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/1ff333eb2a0644ef97769fe03f4afc30/b8a0cb61dda840bfbe0697e8dbcc0cd4/)

Project Description
If we look at a post retrieved from our API, we don’t have any information about the number of comments or likes the post has. As a challenge, I’d like to ask you to add two new fields to retrieved posts for:

1. comments_count
2. likes_count

All of these fields will need to be added to the queryset

2. Product Spec
Now, your challenge is to create the Post fields and Post filters, here’s the spec:

Creating your Post Fields
- In post/views.py, in the PostList class, adjust the queryset to include the following fields:
    1. comments_count
    2. likes_count
- Order the fields by created_at
- In posts/serializers.py:
    1. Define both comments_count and likes_count as ReadOnly fields in the PostSerializer
    2. Include them both in the fields list

Adding Fields to the Filter
- In post/views.py, within the PostList class, create the filter so that you can filter by
    1. comments_count
    2. likes_count
    3. likes__created_at

Adding fields to the PostDetail class
- Adjust the PostDetail queryset to include the following fields:
    1. comments_count
    2. likes_count
- Order the fields by created_at


steps:

Part 1: Creating your PostList Fields
In posts/views.py:
1. Add the required import.
2. In the PostList class, adjust the queryset attribute:
    - Use the annotate function.
    - Define the comments_count field which should Count the number of comments which are distinct.
    - Define the likes_count field which should Count the number of likes that are distinct.
    - Order the annotated fields by how recent Posts are with the most recently created ones first.
In posts/serializer.py
1. Define both comments_count and likes_count as ReadOnly fields in the PostSerializer.
2. Include them both in the fields list.

Part 2: Adding Fields to the Filter
In posts/views.py:
1. Add the required import.
2. Create the filter_backends list, to use OrderingFilter.
3. Add the ordering_fields list, to filter by the appropriate fields.
4. Make sure to add a filter to allow you to sort posts by how recently they've been liked.

Part 3: Adding fields to the PostDetail class
In posts/views.py:
2. In the PostDetail class, copy and paste the PostList queryset into the PostDetail class (removing the existing queryset code).
3. Your new queryset should contain 2 fields: comments_count, likes_count

**[Solution Code](https://github.com/Code-Institute-Solutions/drf-api/tree/a7033eacc714c79df49679fbebd455e300e09d95)**

_____________________________________________________________

## adding a search feature to the API
##### https://youtu.be/_GmXX51kvtY

- create text search for Posts, search either by Author's username or port title
- how to implement text search feature on a view


1. inside `posts`' `views.py` file, in the `PostList` class:
    - add another filter to the `filter_backends` list called `filters.SearchFilter`
    - now, create a new variable called `search_fields` that takes a list of values to search by. in this case it will be `owner__username` to get the owner of a post and `title` for the title of the post
2. run the environment, see if it works. search field should be in the filter button

```py
from django.db.models import Count
from django.shortcuts import render
from django.http import Http404
from rest_framework import status, permissions, generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from drf_api.permissions import IsOwnerOrReadOnly

class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True)

    ).order_by('created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter  # new filter added here
    ]
    ordering_fields = [
        'comments_count',
        'likes_count',
        'likes__created_at',
    ]
    search_fields = [  # new variable for search fields added here
        'owner__username',
        'title',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True)

    ).order_by('created_at')
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'comments_count',
        'likes_count',
        'likes__created_at',
    ]

```

__________________________________________________________________________

## Adding the filter feature to our API
##### https://youtu.be/Xx6JmpgN0qs

- add a filter feature to filter the API data
    - posts owned by a user
    - posts liked by a user
    - posts by another user that a user us following
    - filter user list of accounts a user is following
- using django_filters library

**this section was a bit much trying to understand the traversal of tables, so rewatch the video from 1.52**


### using django_filters

to use filtering methods in this section, the project first needs to have the `django_filters` library installed. install it via the CLI using the following command:
- `pip3 install django-filter`

then, include it in `INSTALLED_APPS` in `settings.py` as `django_filters`

**then, update requirements.txt**: `pip3 freeze > requirements.txt`

to then use `django_filters`, the following import needs to be made on any file wanting to use the library:
- `from django_filters.rest_framework import DjangoFilterBackend`

### add a filter feature to posts:

in the `views.py` of the `posts` app: 

1. import django filters
    - `from django_filters.rest_framework import DjangoFilterBackend`
2. inside the `PostList` view, add `DjangoFilterBackend` to the `filter_backends` list variable
3. create a variable called `filterset_fields` which is a list
    - > To get the user post feed by their profile id, we’ll have to take the following steps: 
    
    > First, we'll have to find out who owns each post in the database. Next, we'll need to see if a post owner is being followed by a specific user. Finally, we'll need to point to that user's profile so that we can use its id to filter our results. 
    
    > Similar to using dot notation from previous sections, we'll have to figure out how to navigate our tables.

#### posts by another user that a user us following

4. to filter posts by another user that a user if following, add the followingvalue to the `filerset_fields` list:
    - refenrence the `owner` of the post, which will give access to the `User` table, 
    - this gives access to referencing the `Follower` table by using the `followed` `related_name`. the `Follower` table can now be queried to see if any entries that have a `followed` value equal to the `Post.owner` and if the person that owns that `followed` value is the accessing user (`owner`, as in `Follower.owner`), then, the accessing `owner`(`Follower.owner`)'s profile is called by using `profile`
    - `'owner__followed__owner__profile'`
    > Model instances can always be filtered by id,  so we don’t need to add “double underscore id”.

#### posts liked by a user

5. as `Post` and `Like` tables are linked by a related_name of `likes`, `likes` can be used to filter to the `owner` of the like, which is a `ForeignKey` linked to the `User` table, which is also linked to the `Profile` table by its own `owner` field
    - `'likes__owner__profile'`

#### posts owned by a user

6. as `Post` is linked to `User` via the `owner` field, the `Profile` table can be accessed directly with double underscore notation
    - `'owner__profile'`

7. add these fields to `filterset_fields` should produce a result like this:

```py
from django.db.models import Count
from django.shortcuts import render
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend  # new filter import here
from rest_framework import status, permissions, generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from drf_api.permissions import IsOwnerOrReadOnly

class PostList(generics.ListCreateAPIView):
    """
    List posts or create a post if logged in
    The perform_create method associates the post with the logged in user.
    """
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True)

    ).order_by('created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,  # new filter added here
    ]
    ordering_fields = [
        'comments_count',
        'likes_count',
        'likes__created_at',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    filterset_fields = [  # new fields added here
        'owner__followed__owner__profile',
        'likes__owner__profile',
        'owner__profile',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a post and edit or delete it if you own it.
    """
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        comments_count=Count('comment', distinct=True),
        likes_count=Count('likes', distinct=True)

    ).order_by('created_at')
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = [
        'comments_count',
        'likes_count',
        'likes__created_at',
    ]
```

### filter user list of accounts a user is following

> We'll be able to filter user profiles that  follow a user with a given profile_id.

1. go to profiles > views, import `from django_filters.rest_framework import DjangoFilterBackend`
2. add `DjangoFilterBackend` to the `filter_backends` list in `ProfileList`
3. create the `filterset_fields` list variable:
    - [watch the walkthrough video from 6.16 to go through the explanation of this with diagrams](https://youtu.be/Xx6JmpgN0qs)
    - add the following filter: `'owner__following__followed__profile'`

updated code:

```py
from django.db.models import Count
from django.http import Http404
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend  # new import added here
from rest_framework import status, generics, permissions, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from drf_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        followers_count=Count('owner__followed', distinct=True),
        following_count=Count('owner__following', distinct=True),
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        DjangoFilterBackend,  #  new filter added here
    ]
    ordering_fields = [
        'post_count',
        'followed_count',
        'following_count',
        'owner__followed__created_at',
        'owner__following__created_at',
    ]
    filterset_fields = [  # new field here
        'owner__following__followed__profile',
    ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
```

_______________________________________________________

## profile filter challenge

- get a list of all of the accounts that follow a user
- in short, it is like getting the accounts a user follows in reverse:
    - `'owner__following__followed__profile'` filters the accounts that a user follows
    - `'owner__followed__owner__profile`