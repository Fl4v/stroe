# Portfolio Website

Portfolio website built using the Dajngo Framework and Bootstrap 4.0 for the templating.

Link to website: [stroe.co.uk](https://stroe.co.uk)

Images from the Media page are stored on a [S3 Bucket](https://aws.amazon.com/s3/)

Webisite is hosted on [DigitalOcean](https://www.digitalocean.com/)

## Documentation links

* To customize the content, design, and features of the site see [Django](https://docs.djangoproject.com/)
* For HTML template design see [Bootstrap](https://getbootstrap.com/)

### Run Development Environment

Set your `.env.dev` file

Example

```
DJANGO_SECRET_KEY=YOUR_SECRET_KEY
DJANGO_DEBUG=0
DJANGO_ALLOWED_HOSTS=0.0.0.0
SQL_ENGINE=django.db.backends.postgresql
SQL_DATABASE=DATABASE_NAME
SQL_USER=DATABASE_USER
SQL_PASSWORD=DATABASE_PASSWORD
SQL_HOST=postgresql_db
SQL_PORT=5432
DATABASE=postgres
POSTGRES_USER=DATABASE_USER
POSTGRES_PASSWORD=DATABASE_PASSWORD
POSTGRES_DB=DATABASE_NAME
```

Build docker images
```
docker-compose build
```

Run docker containers
```
docker-compose up
```

If the containers are running properly, you can access the website at `0.0.0.0`

### Useful CLI Commands

#### Ngnix
```
sudo nano /etc/nginx/sites-available/{project_name} # Access your Nginx config
sudo service nginx status  # Check Nginx status
sudo systemctl restart nginx # Restarts Nginx
sudo nginx -t # Test Nginx config
sudo tail /var/log/nginx/{project_name}.access.log # Check access logs
sudo tail /var/log/nginx/{project_name}.error.log # Check error logs
```
#### Gunicron
```
sudo systemctl restart gunicorn # If change to the Django Application have been made
sudo systemctl status gunicorn # Check gunicorn service status
sudo systemctl daemon-reload
```

#### To-Do

- [ ] Finish docker-compose for production environment
- [ ] Add Gunicorn
- [ ] Add Nginx
- [ ] Add Certbot for SSL
