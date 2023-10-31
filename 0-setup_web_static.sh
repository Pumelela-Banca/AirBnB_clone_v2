#!/usr/bin/env bash
# Creates data directories

sudo apt-get update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
cat > /data/web_static/releases/test/index.html << DATA
<!DOCTYPE html>
<html>
<head>
</head>
    <body>
            <div>Hello from data</div>
    </body>
</html>
DATA
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu /data
chgrp -R ubuntu /data
sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/;}' /etc/nginx/sites-available/default
service nginx restart
exit 0
