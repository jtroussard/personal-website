#!/bin/bash

# Call the sub script to export variables
source ./vars.sh

# Use the exported variables
echo "APP_DIR is set to $APP_DIR"
echo "VENV_DIR is set to $VENV_DIR"
echo "WORKER_COUNT is set to $WORKER_COUNT"

# Define rollback function
rollback() {
    echo "Rolling back changes..."

    # Remove virtual environment directory
    deactivate
    rm -rf venv

    # Remove Nginx config
    sudo rm /etc/nginx/sites-enabled/pw-nginx.conf
    sudo nginx -s reload

    # Remove Supervisor config
    sudo rm /etc/supervisor/conf.d/*
    sudo supervisorctl reload

    # Remove app directory
    sudo rm -rf $APP_DIR

    echo "Rollback complete."
    exit 1
}

# Trap any errors and call rollback function
trap 'rollback' ERR

# Create app directory if it doesn't exist
if [ ! -d $APP_DIR ]; then
	mkdir -p $APP_DIR
fi

# Pull latest release from GitHub
git fetch --tags
git checkout $(git describe --tags `git rev-list --tags --max-count=1`)

# Move project to prod folder
cp -r ./* $APP_DIR
cd $APP_DIR

# Create a virtual environment
python3 -m venv venv
source $VENV_DIR/bin/activate

# Install requirements
pip3 install -r requirements.txt >/dev/null 2>&1

# Configure Nginx
sudo cp $APP_DIR/pw-nginx.conf /etc/nginx/sites-enabled/
sudo systemctl restart nginx
echo "NGINX started"

# Configure Supervisor
sudo cp $APP_DIR/pw-super.conf /etc/supervisor/conf.d/
sudo touch /var/log/personal-website/pw.out.log
sudo touch /var/log/personal-website/pw.err.log
sudo service supervisor start
sudo supervisorctl reload

echo "Deployment complete."
