#!/usr/bin/env bash
#This Bash Script serves web_static Content

#Updates Packages and Installs Nginx if not installed
sudo apt-get update
sudo apt install nginx -y

#Creates Folder if it dooesn't already exist
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

#Creates A simple HTML FILE
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"   | sudo tee /data/web_static/releases/test/index.html

#Creates A Symbolic Link if link doesn't exist
sudo ln -sf /data/web_static/releases/test /data/web_static/current

#Chages Ownership of /data/ folder to ubuntu User and Group
sudo chown -R ubuntu:ubuntu /data/

#Updates Nginx Conf to serve Content of .../current/ to hbnb_static
sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t\tindex index.html;\n\t}\n' /etc/nginx/sites-available/default

#Restarts Nginx Server
sudo service nginx restart
