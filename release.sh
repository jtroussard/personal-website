#!/bin/bash

# Call the sub script to export variables
source ./vars.sh

# Use the exported variables
echo "APP_DIR is set to $APP_DIR"
echo "VENV_DIR is set to $VENV_DIR"
echo "LOG_DIR is set to $LOG_DIR"
echo "WORKER_COUNT is set to $WORKER_COUNT"

# Define rollback function
rollback() {
    echo "Rolling back changes..."

    # Remove virtual environment directory
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
echo "The current working directory is $(pwd)"

# Install requirements
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
echo "Installed project dependencies"

# Configure Nginx
sudo ln -sf $APP_DIR/pw-nginx.conf /etc/nginx/sites-enabled/
sudo systemctl restart nginx
echo "NGINX started"

# Configure Supervisor
sudo ln -sf $APP_DIR/pw-super.conf /etc/supervisor/conf.d/

# Check if directory exists
if [ ! -d $LOG_DIR ]; then
  # Create directory if it doesn't exist
  sudo mkdir -p $LOG_DIR
  # Change ownership of the directory to the current user
  sudo chown -R $USER:$USER $LOG_DIR
  echo "Directory $LOG_DIR created successfully."
else
  echo "Directory $LOG_DIR already exists."
fi

sudo touch /var/log/personal-website/pw.out.log
sudo touch /var/log/personal-website/pw.err.log
sudo service supervisor start
sudo supervisorctl reload
echo "$(sudo service supervisor status)"

echo "Deployment complete."
