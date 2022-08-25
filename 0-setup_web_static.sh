#!/usr/bin/env bash
# set up the web server for the deployment of AirBnB web_static.

sudo apt-get -y update && upgrade
sudo apt-get -y install nginx
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared
echo $'<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>' | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '37i\\tlocation /hbnb_static/ {\nalias /data/web_static/current/;\n}\n' /etc/nginx/sites-available/default
sudo service nginx stop
sudo service nginx start
