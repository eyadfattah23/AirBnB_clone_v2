#!/usr/bin/env bash
# script that sets up your web servers for the deployment of web_static

# Install Nginx if it not already installed
sudo apt-get -y update;
sudo apt-get -y install nginx;

# Create the folder /data/ if it doesn’t already exist
sudo mkdir /data

#Create the folder /data/web_static/ if it doesn’t already exist
sudo mkdir /data/web_static

#Create the folder /data/web_static/releases/ if it doesn’t already exist
sudo mkdir /data/web_static/releases

#Create the folder /data/web_static/shared/ if it doesn’t already exist
sudo mkdir /data/web_static/shared

#Create the folder /data/web_static/releases/test/ if it doesn’t already exist
sudo mkdir /data/web_static/releases/test


#Create a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)

sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

#Create a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder. If the symbolic link already exists, it should be deleted and recreated every time the script is ran.

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user AND group. This should be recursive; everything inside should be created/owned by this user/group.
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo echo "server {
	listen 80;
	listen [::]:80 default_server;
	root   /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name localhost;


    add_header X-Served-By $HOSTNAME;

    location / {
		try_files  / =404;
		}
	location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4/;
    }

    error_page 404 /custom_404.html;
    location = /custom_404.html {
        root /var/www/html;
        internal;
    }
	location /hbnb_static {
		alias /data/web_static/current/;
	}
}

" | sudo tee /etc/nginx/sites-available/default > /dev/null;

sudo service nginx restart;
