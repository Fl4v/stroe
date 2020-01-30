# Portfolio Website

Portfolio website built using the Dajngo Framework and Bootstrap 4.0 for the templating.

## Installation

*Python Version:* 3.8.0

1. Install the software: `pip3 install -r requirements.txt`

## Documentation links

* To customize the content, design, and features of the site see [Django](https://docs.djangoproject.com/).
* For HTML template design see [Bootstrap](https://getbootstrap.com/).

### Useful Django Commands

`django-admin startproject [Project Name]` # Creates new project
`python3 manage.py startapp [APP Name]` # Creates new app in project folder
`python3 manage.py createsuperuser` # Add superuser
`python3 manage.py migrate` # Django migration
`python3 manage.py runserver --settings stroe.settings.prod` # Run server with specific settings file
`python3 manage.py collectstatic` # Collects all static files, including the admin  panel and places then in the static dir

### Useful Deployment CLI Commands

`virtualenv [my_project_venv]` # Creates virtual env
`source [my_project_venv]/bin/activate` # Activates virtual env
`deactivate` # Whilst in the virtual env, use to deactivate

### Ngnix

`sudo nano /etc/nginx/sites-available/{project_name}` # Make changes to your Ngnix file
`sudo service nginx status`  # Check Ngnix status
`sudo systemctl restart nginx` # Restarts Ngnix
`sudo nginx -t` # Test Ngnix config
`sudo tail /var/log/nginx/{project_name}.access.log` # Check access logs
`sudo tail /var/log/nginx/{project_name}.error.log` # Check error logs

### Gunicron

`sudo systemctl restart gunicorn` # If change to the Django Application have been made
`sudo systemctl status gunicorn` # Check gunicorn service status
`sudo systemctl daemon-reload`
`sudo systemctl restart gunicorn`

