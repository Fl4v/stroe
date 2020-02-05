# Portfolio Website

Portfolio website built using the Dajngo Framework and Bootstrap 4.0 for the templating.

Link to website: [stroe.co.uk](https://stroe.co.uk)

Images from the Media page are stored on a [S3 Bucket](https://aws.amazon.com/s3/)
Webisite is hosted on [DigitalOcean](https://www.digitalocean.com/)

## Documentation links

* To customize the content, design, and features of the site see [Django](https://docs.djangoproject.com/)
* For HTML template design see [Bootstrap](https://getbootstrap.com/)

### Run Development Environment

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
sudo nano /etc/nginx/sites-available/{project_name} # Access your 
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
