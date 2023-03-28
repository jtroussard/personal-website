# Personal Website
This repository contains the code for my personal website. The website is built using the Flask web framework and hosted on a Google Cloud Compute Engine instance.

## Getting Started
To run the website locally, you'll need to install the following dependencies:

- Python 3.x
- Flask (pip install Flask)
- gunicorn (pip install gunicorn)
Once you've installed the dependencies, you can start the website by running the following command in the project directory:

`gunicorn app:app`
This will start the website on localhost:8000. You can then view the website in your web browser by navigating to http://localhost:8000.

## Deployment
To deploy the website to a Google Cloud Compute Engine instance, follow these steps:

1. Create a Compute Engine instance in the Google Cloud Console.
1. Clone this repository to your local machine.
1. Copy the contents of the repository to your Compute Engine instance using the gcloud compute scp command. For example:
```
gcloud compute scp --recurse /path/to/local/repository/* \
INSTANCE_NAME:/var/www/personal-website
```
1. SSH into your Compute Engine instance using the gcloud compute ssh command. For example:
```
gcloud compute ssh INSTANCE_NAME
```
1. Install the website dependencies by running the following commands:
```
cd /var/www/personal-website
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```
1. Start the website using gunicorn by running the following command:
```
gunicorn app:app
```
This will start the website on port 80.
1. Finally, configure your domain name to point to the external IP address of your Compute Engine instance.