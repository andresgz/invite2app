Invite2App
===================

Allows to Invite your Facebook friends to your application.
Application using Django 1.8, Django Rest framework and angularJS.

Demo: http://ec2-52-89-15-237.us-west-2.compute.amazonaws.com/  


Application Setup
==================

Uses Django 1.8.4, and the requirements are specified in the requirements.txt file

Uses PostgresSQL. An empty Database is required to run migrations.

To configure Database set the Enviroment variable DATABASE_URL. For example:

    export DATABASE_URL=postgres://example_user:password@localhost:5432/invite2app

1. Populate Database:
---------------------

    python manage.py migrate


2. Create Super User:
---------------------

    python manage.py createsuperuser


3. Run Development Server
-------------------------

    python manage.py runserver

The application will run at http://localhost:8000

4. Configure Facebook application
---------------------------------

Log in as administrator with the previous account and configure the Facebook app at:

http://localhost:8000/admin/socialaccount/socialapp/add/

Provide the Facebook credentials in the fields: Client id and Secret key as follows:

    Django Admin :  Facebook App
    Client id    :  App ID
    Secret key   :  App Secret


5. Additional Enviroment Variables
-----------------------------------

These variables are optional and required for the Facebook JS SDK to be defined explicitly. Bye default, it uses local values.

    APP_URL             :  Url of the application
    FACEBOOK_APP _ID    :  Facebook application id obtained in last step 
    INVITE_MESSAGE      :  Custom message of the Invite Message

6. Front-end configuration
--------------------------

Make sure that nodejs is installed. Then in the project root run:

    npm install

Now you just need:

    grunt serve

The base app will now run as it would with the usual manage.py runserver but with live reloading and Sass compilation enabled.

The Front-end application runs inside the Django Template System. In order to get the required front-end libraries, we use bower.
        
    npm -g install bower
    bower install


Path of front-end libraries: invite2app/static/bower_components

Run Unit Tests
--------------

    python manage.py test



Deployment to Production on AWS
-------------------------------

System requirements for Debian based servers: requirements.apt

Python requirements: requirements.txt

In order to run this application in production. The following environment variables need to be defined:

    DJANGO_SETTINGS_MODULE
    DJANGO_SECRET_KEY
    DJANGO_AWS_ACCESS_KEY_ID
    DJANGO_AWS_SECRET_ACCESS_KEY
    DJANGO_AWS_STORAGE_BUCKET_NAME
    DATABASE_URL
    APP_URL
    FACEBOOK_APP_ID
    INVITE_MESSAGE


It was succesfully tested and mounted on AWS using Python Virtualenv, UWSGI and NGINX.

UWSGI Configuration
-------------------

    [uwsgi]
    vhost = true
    plugins = python
    socket = /tmp/invite2app.sock
    master = true
    enable-threads = true
    processes = 4
    wsgi-file = /srv/apps/invite2app/config/wsgi.py
    virtualenv = /home/ubuntu/.virtualenvs/env
    chdir = /srv/apps/invite2app/
    env = DJANGO_SETTINGS_MODULE=config.settings.production
    env = DJANGO_SECRET_KEY=###CUSTOM_VALUE###
    env = DJANGO_AWS_ACCESS_KEY_ID=###CUSTOM_VALUE###
    env = DJANGO_AWS_SECRET_ACCESS_KEY=###CUSTOM_VALUE###
    env = DJANGO_AWS_STORAGE_BUCKET_NAME=###CUSTOM_VALUE###
    env = DATABASE_URL=postgres://db_user:db_password@DATABASE_SERVER_HOST:5432/invite2app
    env = APP_URL=http://ec2-52-89-15-237.us-west-2.compute.amazonaws.com
    env = FACEBOOK_APP_ID=###CUSTOM_VALUE###
    env = INVITE_MESSAGE="Te invito a Invite2APP en http://ec2-52-89-15-237.us-west-2.compute.amazonaws.com"

Nginx Configuration
-------------------

    server {
        listen 80;
        access_log /var/log/nginx/invite2app.access.log;
        error_log /var/log/nginx/invite2app.error.log;

        location / {
            uwsgi_pass      unix:///tmp/invite2app.sock;
            include     uwsgi_params;
        }
    }


The used services were:

    Amazon EC2
    Amazon RDS PostgresSQL
    Amazon S3
