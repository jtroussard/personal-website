#!/bin/bash

# Pull latest release from GitHub
git fetch --tags
git checkout $(git describe --tags `git rev-list --tags --max-count=1`)

# Activate venv
source venv/bin/activate

# Install requirements
pip3 install -r requirements.txt

# Reboot Nginx
sudo ln -s ./pw-nginx.conf /etc/nginx/sites-enabled/
sudo nginx -s reload

# Reboot supervisor
sudo ln -s ./pw-supervisor.conf /etc/supervisor/conf.d/
sudo supervisorctl reload
