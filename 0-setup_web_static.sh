#!/usr/bin/env bash
# Bash script that sets up a web server with specific configuration
sudo apt-get -y update
sudo apt-get -y install nginx
sudo mkdir /data
sudo mkdir /data/web_static
sudo mkdir /data/web_static/releases
sudo mkdir /data/web_static/shared
sudo mkdir /data/web_static/releases/test
sudo touch /data/web_static/releases/test/index.html
sudo print %s "
<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>
" >> /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i "49i location \/hbnb_static {\n\t\talias /data/web_static/current;\n\t}" /etc/nginx/sites-available/default
sudo service nginx restart
