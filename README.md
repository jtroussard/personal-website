# Summary

This repository contains the code for my personal website. The website is built using the Flask web framework and hosted on a Google Cloud Compute Engine instance. All commands and examples provided in terms of a UNIX based system. Should work fine on a windows machine but will require some additional homework to handle the difference in terminal environments, commands, and string paths.

# Getting Started

## Dependencies

To run the website locally, you'll need to install the following dependencies:

- Python 3.x
- Flask (pip install Flask)
- gunicorn (pip install gunicorn)

# SETUP SECTION WIP
## Development Setup

- Clone repository
- Create `.env` directory
- set preconfig env variables
  - PROGRAM_ENV
  - LOCATION_ENV
  - KAGIS: This is where you put your service account keys for development mode
## Production Setup
`/etc/supervisor/conf.d/{application specific conf for supervisor file name}`
- set PROGRAM_ENV
- set LOCATION_ENV

## Content Interpolation

Previous version of this application loaded content in category chunks via files servered from the host serve. They are now accessed via a google cloud bucket, acting as a private CDN. Updates to the content is performed via object upload to the bucket.

No more setting content file paths via configurations. This will be updated as part of a clean up branch in the near future.

Create the content files, [fill them out as per the schema described here](#configuration), then upload to the target bucket.

__HINT__ empty demo content files are located in the `doc/` directory. <=== no longer relevant but still need to doc development content delivery




## Deployment (Needs updating)

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



# Version 2 Design Proposal/Notes

~~## Replace content files with private api service~~

~~Implment an PI Integration for Private Content. This will allow for the content files to be managed separately by another private. By decoupling private content from the public-facing application, this can enhance security and version control for content files. Here are some notes on implementation.~~

Went with a sort of private CDN with signed URLs. Good learning experience, and I think does the job quite well.