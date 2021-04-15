#!/usr/bin/env bash
# This script sets up your web servers for the deployment of web_static
apt-get update
mkdir -p /data/
mkdir -p /data/web_static/
mkdir -p /data/web_static/releases/
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/
echo " <h1 align="center"> Cool You Nginx configuration is ready 🦾</h1> " > /data/web_static/releases/test/index.html
ln -s -f /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
# Install Nginx in my server
apt-get -y install nginx
# config hbnb_static as alias
sed -i '/listen 80 default_server/a location /hbnb_static/ { alias /data/web_static/current/; }' /etc/nginx/sites-available/default
# restarts the server
service nginx restart
