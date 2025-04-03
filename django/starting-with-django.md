# Django Getting Started

## Prerequisites

- To install Django, you must have Python installed, and a package manager like PIP. PIP is included in Python from version 3.4.

### Check If You Got Python

To check if your system has Python installed, run this command in the command prompt:

        `python --version`

if not installed. Install python. On Ubuntu Linux use the command:

        `sudo apt update`

        `sudo apt install python3`

Verify Installation: You can verify the installation by checking the Python version:

        `python3 --version`

### Install PIP

To install Django, you must use a package manager like PIP, which is included in Python from version 3.4.

To check if your system has PIP installed, run this command in the command prompt:

        `pip --version`

## Virtual Environment

It is suggested to have a dedicated virtual environment for each Django project. Create a virtual environment, and then install Django in it.

To create a virtual environment, decide upon a directory where you want to place it, and run the `venv` module as a script with the directory path:

A common directory location for a virtual environment is `.venv`. This name keeps the directory typically hidden in your shell and thus out of the way while giving it a name that explains why the directory exists. It also prevents clashing with .env environment variable definition files that some tooling supports.

        `python -m venv .venv`

Once you’ve created a virtual environment, you may activate it. On Unix or MacOS, run:

        `source .venv/bin/activate`

As for VsCode editor it might prompt you to activate.

Activating the virtual environment will change your shell’s prompt to show what virtual environment you’re using, and modify the environment so that running python will get you that particular version and installation of Python. For example:

        `$ source .venv/bin/activate`
        `(.venv) $ python Pyton 3.5.1`

To deactivate a virtual environment, type:

        `deactivate`

into the terminal.


## Install Django

Now, that we have created a virtual environment, we are ready to install Django. Note: Remember to install Django while you are in the virtual environment!

Django is installed using pip, with this command:

        `python -m pip install Django`

Check the version:

### Check Django Version

You can check if Django is installed by asking for its version number like this:

        `(.venv) kulimanje@Bwanji:~/repos/PyZilla/django$ django-admin --version`


## Django Create Project

Run this command in the command prompt:

        `django-admin startproject first_django_app`

## Run the Django Project

Now that you have a Django project, you can run it, and see what it looks like in a browser.

Navigate to the `/first_django_app` folder and execute this command in the command prompt:

        `python manage.py runserver`

## Django Create App

You cannot have a web page created with Django without an app. 

### What is an App?

An app is a web application that has a specific meaning in your project, like a home page, a contact form, or a members database.

In this tutorial we will create an app that allows us to list and register members in a database.

But first, let's just create a simple Django app that displays "Hello World!".

### Create App

I will name my app `members`. Start by navigating to the selected location where you want to store the app.

        `python manage.py startapp members`

## Views

Django views are Python functions that take http requests and return http response, like HTML documents.

A web page that uses Django is full of views with different tasks and missions.

Views are usually put in a file called views.py located on your app's folder.

There is a views.py in your members folder that looks like this:

        `first_django_app/members/views.py`

Find `views.py` it and open it, and replace the content with this:

        `from django.shortcuts import render
        from django.http import HttpResponse

        def members(request):
        return HttpResponse("Hello world!")`

## Django URLs

Create a file named `urls.py` in the same folder as the `views.py` file, and type this code in it:


        `from django.urls import path
        from . import views

        urlpatterns = [
        path('members/', views.members, name='members'),
        ]`

The `urls.py` file you just created is specific for the `members` application. We have to do some routing in the root directory `first_django_app` as well. This may seem complicated, but for now, just follow the instructions below.

There is a file called `urls.py` on the `first_django_app` folder, open that file and add the `include` module in the `import` statement, and also add a `path()` function in the `urlpatterns[]` list, with arguments that will route users that comes in via `127.0.0.1:8000/`.

Then your file will look like this:

`first_django_app/first_django_app/urls.py`:

        `from django.contrib import admin
        from django.urls import include, path

        urlpatterns = [
        path('', include('members.urls')),
        path('admin/', admin.site.urls),
        ]`
        

## Templates

Create a `templates` folder inside the `members` folder, and create a HTML file named `myfirst.html`.

Open the HTML file and insert the following:

        `<!DOCTYPE html>
        <html>
        <body>
        
        <h1>Hello World!</h1>
        <p>Welcome to my first Django project!</p>
        
        </body>
        </html>`

## Modify the View

Open the `views.py` file in the `members` folder, and replace its content with this:

`my_first_django_app/members/views.py:`

        `from django.http import HttpResponse
         from django.template import loader
    
            def members(request):
              template = loader.get_template('myfirst.html')
              return HttpResponse(template.render())`


## Change Settings

To be able to work with more complicated stuff than "Hello World!", We have to tell Django that a new app is created.

This is done in the `settings.py` file in the `my_tennis_club` folder.

Look up the `INSTALLED_APPS[]` list and add the `members` app like this:

`my_tennis_club/my_tennis_club/settings.py:`

    `INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'members'
    ]`

Then run this command:

        `python manage.py migrate`

Which will produce this output:

    `Operations to perform:
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
          Applying auth.0010_alter_group_name_max_length... OK
          Applying auth.0011_update_proxy_permissions... OK
          Applying auth.0012_alter_user_first_name_max_length... OK
          Applying sessions.0001_initial... OK
        
    (myworld) C:\Users\Your Name\myworld\my_tennis_club>`

Start the server by navigating to the /first_django_app folder and execute this command:

        `python manage.py runserver`

## Django Models

A Django model is a table in your database.

Up until now in this tutorial, output has been static data from Python or HTML templates.

Now we will see how Django allows us to work with data, without having to change or upload files in the process.

In Django, data is created in objects, called Models, and is actually tables in a database.

### Create Table (Model)

To create a model, navigate to the `models.py` file in the `/members/` folder.

Open it, and add a `Member` table by creating a `Member class`, and describe the table fields in it:

`my_tennis_club/members/models.py:`

        `from django.db import models

        class Member(models.Model):
          firstname = models.CharField(max_length=255)
          lastname = models.CharField(max_length=255)`

The first field, `firstname`, is a Text field, and will contain the first name of the members.

The second field, `lastname`, is also a Text field, with the member's last name.

Both `firstname` and `lastname` is set up to have a maximum of 255 characters.

## SQLite Database
When we created the Django project, we got an empty SQLite database.

It was created in the `first_django_app` root folder, and has the filename `db.sqlite3`.

By default, all Models created in the Django project will be created as tables in this database.


## Migrate

Now when we have described a Model in the `models.py` file, we must run a command to actually create the table in the database.

Navigate to the `first_django_app` folder and run this command:

        `python manage.py makemigrations members`

Which will result in this output:

        `Migrations for 'members':
          members\migrations\0001_initial.py
            - Create model Member
        
        (myworld) C:\Users\Your Name\myworld\my_tennis_club>`


Django creates a file describing the changes and stores the file in the `/migrations/` folder:

`my_tennis_club/members/migrations/0001_initial.py`:

        `# Generated by Django 5.1.7 on 2025-03-20 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
            ],
        ),
    ]`

Note that Django inserts an `id` field for your tables, which is an `auto increment number` (first record gets the value 1, the second record 2 etc.), this is the default behavior of Django, you can override it by describing your own `id` field.

The table is not created yet, you will have to run one more command, then Django will create and execute an SQL statement, based on the content of the new file in the `/migrations/` folder.

Run the migrate command:

        `python manage.py migrate`

Which will result in this output:

        `Operations to perform:
          Apply all migrations: admin, auth, contenttypes, members, sessions
        Running migrations:
          Applying members.0001_initial... OK
        
        (myworld) C:\Users\Your Name\myworld\my_tennis_club>`

Now you have a `Member` table in you database!

### View SQL

As a side-note: you can view the SQL statement that were executed from the migration above. All you have to do is to run this command, with the migration number:

        `python manage.py sqlmigrate members 0001`

Which will result in this output:

        `BEGIN;
        --
        -- Create model Member
        --
        CREATE TABLE "members_member" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "firstname" varchar(255) NOT NULL, "lastname" varchar(255) NOT NULL);
        COMMIT;`

