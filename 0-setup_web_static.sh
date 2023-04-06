#!/usr/bin/env bash
#install Nginx if not already installed
if ! dpkg -s nginx &> /dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

# Create directories and files for web_static deployment
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo " <html>
		 < head>
		  </head>
		  < body>
			Holberton school
		  </body>
		</html>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership 
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i '/listen 80 default_server;/a \\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
