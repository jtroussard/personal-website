#!/bin/bash

echo "Checking if Nginx is installed..."
if ! command -v nginx &> /dev/null
then
    echo "Nginx is not installed, updating repo list and installing..."
    sudo apt update && sudo apt install -y nginx
else
    echo "Nginx is already installed."
fi

echo "Checking if Supervisor is installed..."
if ! command -v supervisorctl &> /dev/null
then
    echo "Supervisor is not installed, updating repo list and installing..."
    sudo apt update && sudo apt install -y supervisor
else
    echo "Supervisor is already installed."
fi

echo "Checking if Python 3 is installed..."
if ! command -v python3 &> /dev/null
then
    echo "Python 3 is not installed, updating repo list and installing..."
    sudo apt update && sudo apt install -y python3
else
    echo "Python 3 is already installed."
fi

echo "Installation complete."
echo "Nginx version:"
nginx -v
echo "Supervisor version:"
supervisorctl -v
echo "Python 3 version:"
python3 --version
