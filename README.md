# Summary

This repository contains the code for my personal website. The website is built using the Flask web framework and hosted on a Google Cloud Compute Engine instance. All commands and examples provided in terms of a UNIX based system. Should work fine on a windows machine but will require some additional homework to handle the difference in terminal environments, commands, and string paths.

# Getting Started

## Dependencies

To run the website locally, you'll need to install the following dependencies:

- Python 3.x
- Flask (pip install Flask)
- gunicorn (pip install gunicorn)

## Required Configurations

Content for this website is provided via simple json files.

Create the content files, [fill them out as per the schema described here](#configuration), then run these terminal commands to tell the flask appliction where to load the files from:

```bash
export PORTFOLIO_DATA_PATH=./personal_website/portfolio.json
export SOCIAL_DATA_PATH=./personal_website/social.json
```

__HINT__ empty demo content files are located in the `doc/` directory.

## Starting the Server (Development Mode)

```bash
python run.py`
```

or if you preferr to use flask

```bash
export FLASK_APP=personal_website
flask run
```

You can modify your server passing options to the flask command like this...

```bash
flask run --debug --port 12345
```

## Deployment

To deploy the website to a Google Cloud Compute Engine instance, follow these steps:

1. Create a Compute Engine instance in the Google Cloud Console.
1. Clone this repository to your local machine.
1. Copy the contents of the repository to your Compute Engine instance using the gcloud compute scp command. For example:

```bash
$ gcloud compute scp --recurse /path/to/local/repository/* INSTANCE_NAME:/home/${whoami}/personal-website
```

1. SSH into your Compute Engine instance using the gcloud compute ssh command. For example:

```bash
$ gcloud compute ssh INSTANCE_NAME
```

1. Install the website dependencies by running the following commands:

```bash
cd /home/${whoami}/personal-website
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

1. Start the website using gunicorn by running the following command:

```bash
gunicorn app:app
```

This will start the website on port 80.

1. Finally, configure your domain name to point to the external IP address of your Compute Engine instance.

## Configuration

### Content files JSON Schema

Several content files are used to interpolate data. This is to allow for single point of updates and to allow for future flexibility. All content files need to be provided, as they are critical for the use case of this web application. No defaults or error checking for the completeness of this data is provided. Additionally these paths need to be set for the application to boot correcly.

* `PORTFOLIO_DATA_PATH`
* `SOCIAL_DATA_PATH`

No defaults for these either.

### List of required content files

- `portfolio.json`: Used to populate the resume data content of the application.
- `social.json`: Used to populate and configure any driving data for social media links, icons, etc.

The schema guide below describes the structure and fields of the content files.

### JSON Data Schema: portfolio.json

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
        "required": [
          "title",
          "company",
          "duration",
          "description",
          "location",
          "workplace"
        ]
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

### JSON Data Schema: social.json

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "name": {
        "type": "string"
      },
      "url": {
        "type": "string",
        "format": "uri"
      },
      "fontAwesomeIcon": {
        "type": "string"
      },
      "icon": {
        "type": "string"
      },
      "color": {
        "type": "string",
        "pattern": "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
      },
      "text": {
        "type": "string"
      },
      "textColor": {
        "type": "string",
        "pattern": "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
      },
      "backgroundColor": {
        "type": "string",
        "pattern": "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
      },
      "hoverBehavior": {
        "type": "string",
        "enum": ["darker", "lighter"]
      }
    },
    "required": [
      "name",
      "url",
      "fontAwesomeIcon",
      "icon",
      "color",
      "text",
      "textColor",
      "backgroundColor",
      "hoverBehavior"
    ]
  }
}
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

# Version 2 Design Proposal/Notes

## Replace content files with private api service

Implment an PI Integration for Private Content. This will allow for the content files to be managed separately by another private. By decoupling private content from the public-facing application, this can enhance security and version control for content files. Here are some notes on implementation.

### Dedicated Private API Service:

Design a separate Flask application to act as the Private API Service.
Host this service in a private network or behind a firewall for added security.
Handle authentication and authorization to restrict access to authorized users (public-facing app).

### Secure Communication:

Use encryption protocols (e.g., HTTPS) to ensure secure communication between the public-facing app and Private API Service. Have some experience using Let's Encrypt for this kind of stuff. Implement access controls and API keys for authorized requests.

### Private Content Repository:

Set up a private repository to store content files securely.
Use version control to track changes, collaborate, and maintain data consistency.

### API Documentation:

Prepare detailed API documentation for the Private API Service to facilitate integration with the public-facing app.
Include guidelines for handling private content requests and responses.

### Design Considerations:

#### Authentication Mechanism:

Explore token-based authentication (e.g., JWT) to verify user access to private content.
Additional research for OAuth 2.0 for handling third-party integrations if required.

#### Private Network Configuration:

Work with DevOps team to configure the private network securely.
Implement VPN for remote access to the Private API Service during development and testing.

#### Version Control Strategies:

Adopt Git branching and merging strategies for content files version control.
Use semantic versioning for content releases to ensure backward compatibility.

#### Error Handling and Logging:

Implement comprehensive error handling for API requests and responses.
Set up logging mechanisms to monitor and troubleshoot issues.

#### Tech Stack:

Flask (Python) for both the public-facing app and Private API Service.
GitLab: Try something different and show how code resources can be managed on different platforms and still work together. If for any reason, just to say I can do it xD
Docker for containerization and easy deployment.