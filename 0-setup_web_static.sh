#!/usr/bin/env bash
# script that sets up web servers for the deployment of web_static

# 1. Install Nginx if it not already installed
sudo apt-get -y update
sudo apt-get -y install nginx

# 2. Create the folder /data/web_static/releases/test and it's parents if not already exist
sudo mkdir -p /data/web_static/releases/test/

# 3. Create the folder /data/web_static/shared/ if it doesn’t already exist
sudo mkdir -p /data/web_static/shared/

# 4. Create a fake HTML file (to test your Nginx configuration)
echo "Melius will be alive soon!!" | sudo tee /data/web_static/releases/test/index.html >/dev/null

# 5. Create a symbolic link /data/web_static/current to the releases/test/
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# 6. Give ownership of the /data/ folder to the ubuntu user AND group
sudo chown -R ubuntu:ubuntu /data/

# 7. Update the Nginx configuration to serve the content
sudo sed -i '59i\\tlocation \/hbnb_static { \n\t\talias \/data\/web_static\/current/;\n\t}' /etc/nginx/sites-available/default

#8. Restart the Nginx server
sudo service nginx restart;
