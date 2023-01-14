#!/usr/bin/env bash
# sets up web servers for deloyment of web-static

sudo apt-get install -y nginx
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

echo "
<html>
  <head>
  </head>
  <body>
    Hello World!
  </body>
</html>" >> /data/web_static/releases/test/index.html
sudo ln -s -Ff /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

sudo sed -i "38i\ \tlocation \/hbnb_static {\\n\\t\\talias \/data\/web_static\/current\/;\\n}" /etc/nginx/sites-available/default
sudo service nginx restart
