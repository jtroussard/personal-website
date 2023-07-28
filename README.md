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
INSTANCE_NAME:/home/${whoami}/personal-website
```
1. SSH into your Compute Engine instance using the gcloud compute ssh command. For example:
```
gcloud compute ssh INSTANCE_NAME
```
1. Install the website dependencies by running the following commands:
```
cd /home/${whoami}/personal-website
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

## Configuration

### Portfolio Data JSON Schema

The JSON file contains data for this portfolio website and is used by the Flask application interpolate resume content. The schema guide below describes the structure and fields of the JSON data.

### JSON Data Schema:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "name": { "type": "string" },
    "tagline": { "type": "string" },
    "location": { "type": "string" },
    "email": { "type": "string", "format": "email" },
    "linkedin": { "type": "string", "format": "uri" },
    "about_header": { "type": "string" },
    "about": { "type": "string" },
    "spoken_languages": {
      "type": "array",
      "items": { "type": "string" }
    },
    "summary": { "type": "string" },
    "experiences": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "title": { "type": "string" },
          "company": { "type": "string" },
          "duration": { "type": "string" },
          "description": { "type": "string" },
          "details": {
            "type": "array",
            "items": { "type": "string" }
          },
          "location": { "type": "string" },
          "workplace": { "type": "string" }
        },
        "required": ["title", "company", "duration", "description", "location", "workplace"]
      }
    },
    "education": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "institution": { "type": "string" },
          "degree": { "type": "string" },
          "concentration": { "type": "string" },
          "location": { "type": "string" }
        },
        "required": ["institution", "degree", "location"]
      }
    },
    "licenses_certifications": {
      "type": "array",
      "items": { "type": "string" }
    },
    "skills": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "display_name": { "type": "string" },
          "name": { "type": "string" },
          "experience": { "type": "string", "format": "date" }
        },
        "required": ["display_name", "name", "experience"]
      }
    },
    "honors_awards": {
      "type": "array",
      "items": { "type": "string" }
    }
  },
  "required": [
    "name",
    "tagline",
    "location",
    "email",
    "linkedin",
    "about_header",
    "about",
    "spoken_languages",
    "summary",
    "experiences",
    "education",
    "licenses_certifications",
    "skills",
    "honors_awards"
  ]
}

```

### Saving the JSON File on Compute Engine:

Copy the JSON file (data.json) to the Compute Engine instance using scp:

```bash
scp /path/to/data.json your_username@compute-engine-instance-ip:/etc/personal-website/
```

Create the directory for configuration files:

```bash
sudo mkdir /etc/personal-website
```

Move the JSON file to the new directory and set appropriate permissions:

```bash
sudo mv data.json /etc/personal-website/
sudo chmod 600 /etc/personal-website/data.json
```

### Setting the Environment Variable on Compute Engine:

To set the PORTFOLIO_DATA_PATH environment variable on your Compute Engine instance, follow these steps:

SSH into your Compute Engine instance:

```bash
gcloud compute ssh your-instance-name
```

Set the environment variable to point to the JSON file path:

```bash
export PORTFOLIO_DATA_PATH=/etc/personal-website/data.json
```

Optionally, add the above command to the user's .bashrc or .bash_profile file to set the variable automatically on login.

Now your Flask application running on the Compute Engine instance will have access to the JSON data file via the PORTFOLIO_DATA_PATH environment variable. Remember to replace your-instance-name with the appropriate value.