"""
Docstring this later
"""
import requests
from personal_website.content.sign_urls import signed_url_generator

class ContentLoader:
    """
    Class: ContentLoader
    Description: Loads content from a Google Cloud Storage bucket.
    """
    def __init__(self, app_config, logger):
        """
        Constructor: ContentLoader
        Description: Initializes the ContentLoader class.
        :param app_config: The app configuration object.
        :param logger: The logger object.
        """
        self.app_config = app_config
        self.logger = logger

    def generate_signed_url(self, file_name, sub_bucket, force_refresh=True):
        """
        Function: generate_signed_url
        Description: Generates a signed URL for an asset stored in Google Cloud Storage.
        :param file_name: The name of the file.
        :param sub_bucket: The sub-bucket where the file is stored.
        :param force_refresh: Whether to force a refresh of the signed URL.
        :return: The signed URL.
        """
        bucket_path = f"{sub_bucket}/{file_name}" if sub_bucket else file_name
        return signed_url_generator(
            environment=self.app_config["ENVIRONMENT"],
            logger=self.logger,
            bucket=self.app_config["BUCKET_NAME"],
            bucket_path_to_file=bucket_path,
            kagis=self.app_config["KAGIS"],
            force_refresh=force_refresh,
        )

    def load_json(self, file_name, force_refresh=True):
        """
        Function: load_json
        Description: Loads a JSON file from a Google Cloud Storage bucket.
        :param file_name: The name of the file.
        :param force_refresh: Whether to force a refresh of the signed URL.
        :return: The JSON data.
        """
        sub_bucket = "content"
        url = self.generate_signed_url(
            file_name=file_name, sub_bucket=sub_bucket, force_refresh=force_refresh
        )
        json_data = requests.get(url, timeout=15).json()
        return json_data

    def load_css(self, file_name, force_refresh=True):
        """
        Function: load_css
        Description: Loads a CSS file from a Google Cloud Storage bucket.
        :param file_name: The name of the file.
        :param force_refresh: Whether to force a refresh of the signed URL.
        :return: The CSS data.
        """
        sub_bucket = "css"
        url = self.generate_signed_url(
            file_name=file_name, sub_bucket=sub_bucket, force_refresh=force_refresh
        )
        css_data = requests.get(url, timeout=15).text
        return css_data

    def load_image(self, file_name, force_refresh=True):
        """
        Function: load_image
        Description: Loads an image file from a Google Cloud Storage bucket.
        :param file_name: The name of the file.
        :param force_refresh: Whether to force a refresh of the signed URL.
        :return: The image data.
        """
        sub_bucket = "images"
        url = self.generate_signed_url(
            file_name=file_name, sub_bucket=sub_bucket, force_refresh=force_refresh
        )
        image_data = requests.get(url, timeout=15).content
        return image_data
