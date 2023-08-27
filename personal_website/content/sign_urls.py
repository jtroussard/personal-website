"""
Module: sign_urls
Description: Provides utility functions for generating signed URLs for assets stored in Google Cloud Storage.
"""
from google.cloud import storage
from google.auth import compute_engine

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
        # GCP Docs where dog shit on this process. Answer was in front of me the whole
        # but was trying to follow some principles and the docs. Just store the key as a
        # secret and pass it to the sotrage client. This ACP or auto authentication
        # from the compute engine (mentioned in docs) is a giant pile of poo. And if
        # there is a receipt to authenticate another way it isn't obvious and the docs 
        # are a little bit all over the place so it is espically hard to line up
        # the documentaion aritcles so that they all represent good and correct 
        # information when taking into consideration your use case, 
        # source resource type/env/service account/destination resource type... etc
        storage_client = storage.Client.from_service_account_json(kagis)
        credentials_info = storage_client._credentials.to_authorized_user_info()
        logger.info(f"gcp authentication in DEVELOPMENT mode")

    elif environment == "production":
        credentials = compute_engine.Credentials()
        storage_client = storage.Client.from_service_account_json(kagis)
        logger.info(f"gcp authentication in PRODUCTION mode")
    else:
        logger.error(f"invalid environment: {environment}")

    # TODO: What to make this more elegant but for now just going to leave the tap on
    # until I am more confident in the authentication pattern I am following
    # (see above rant) then I will return to this and save myself a call based
    # on the expiration diff of the signed url.
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