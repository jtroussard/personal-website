"""
Module: sign_urls
Description: Provides utility functions for generating signed URLs for assets stored in Google Cloud Storage.
"""

from google.cloud import storage

def signed_url_generator(
    environment, logger, bucket, bucket_path_to_file, kagis, force_refresh=False
):
    """
    Function: signed_url_generator
    Description: Generates a signed URL for an asset stored in Google Cloud Storage.
    :param environment: The current environment ("development" or "production").
    :param logger: The logger object.
    :param bucket: The name of the Google Cloud Storage bucket.
    :param bucket_path_to_file: The path to the file within the bucket.
    :param kagis: The path to the service account key file.
    :param force_refresh: Whether to force a refresh of the signed URL.
    :return: The signed URL.
    """
    if environment == "development":
        # Load the service account key explicitly for development environments.
        # Pass the path to the service account key file downloaded from GCP.
        storage_client = storage.Client.from_service_account_json(kagis)
        logger.info("storage client in developer mode")
    else:
        # Docs state compute engine in production env auto authenticates the
        # service account for "free"
        # https://cloud.google.com/docs/authentication/provide-credentials-adc#attached-sa
        storage_client = storage.Client()

    # TODO: I wanted to be more elegant here but I will open an issue and revisit this
    # conditional later, stuck in the on positions for now
    if force_refresh:
        bucket_name = bucket
        blob = storage_client.bucket(bucket_name).blob(bucket_path_to_file)
        signed_url = blob.generate_signed_url(
            version="v4",
            expiration=5,
            method="GET",
        )
    logger.info(f"generate_signed_url invoked for resource {bucket_path_to_file}")
    return signed_url
