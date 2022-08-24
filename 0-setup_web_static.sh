#!/usr/bin/env bash
# set up the web server for the deployment of AirBnB web_static.

sudo apt-get -y update && upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
cfg=\
"<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"
echo "$cfg" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx stop
sudo service nginx start
