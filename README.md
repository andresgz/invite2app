Invite2App
===================

Allows to Invite your Facebook friends to your application.
Application using Django 1.8, Django Rest framework and angularJS.

Demo:


Django Application
==================

Uses Django 1.8.4, and the requirements are specified in the requirements.txt file

Uses PostgresSQL. An empty Database is required to run migrations.

To configure Database set the Enviroment variable DATABASE_URL. For example:

    export DATABASE_URL=postgres://example_user:password@localhost:5432/invite2app

Populate Database:
------------------

    python manage.py migrate

Run application locally
-----------------------

    python manage.py runserver
    or
    grunt serve

The API application will run in http://localhost:8000

Run Unit Tests
--------------
    python manage.py test



Front-edn Application
=====================

The Front-end application runs inside the Django Templates System. In order to get the front-end libraries you need to have previously installed NODEJS. Then you can install the dependencies using bower:
        
    npm -g install bower
    bower install


Path of front-end libraries: invite2app/static/bower_components

SASS compilation and LiveReload
-------------------------------

Run the project with grunt serve:

    grunt serve


Set APP URL:
You need to define the enviroment variable APP_URL with the value of the URL of the app. It's required for Facebook interactions

    export APP_URL=http://localhost:8000


Deploy to AWS
-------------

    grunt deploy
Environment variables required from the AWS S3 Bucket:

    AWS_ACCESS_KEY_ID, 
    AWS_SECRET_ACCESS_KEY,
    AWS_STORAGE_BUCKET_NAME

Run AngularJS Test
------------------

    npm test

Deployment to Production on AWS
-------------------------------

The API application can be deployed using Docker. The specifications are in the file docker-compose.yml

System requirements for Debian based servers: requirements.apt

Python requirements: requirements.txt

In order to run this application in production. The following environment variables need to be defined:

DJANGO_SETTINGS_MODULE
DJANGO_SECRET_KEY
DJANGO_ALLOWED_HOSTS
DJANGO_AWS_ACCESS_KEY_ID
DJANGO_AWS_SECRET_ACCESS_KEY
DJANGO_AWS_STORAGE_BUCKET_NAME
DJANGO_DATABASE_URL

It was succesfully tested and mounted on AWS using Python Virtualenv, UWSGI and NGINX.

The used services were:
Amazon EC2
Amazon RDS PostgresSQL
Amazon S3
