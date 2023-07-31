# pylint: disable=import-error, no-member, missing-module-docstring
import os
from flask import url_for, current_app as app

def get_icon_url(input_string):
    """
    Jinja2 filter: Get the URL for an icon based on the input string.
    :param input_string: The input string.
    :return: The URL for the icon.
    """
    # Define the directory where the icons are stored
    icons_directory = os.path.join(app.static_folder, 'images', 'icons')

    # Construct the expected icon filename format
    icon_filename = f"icons8-{input_string.lower()}-50.png"

    # Check if the file exists in the icons directory
    icon_filepath = os.path.join(icons_directory, icon_filename)

    if os.path.exists(icon_filepath):
        # Return the URL for the icon
        app.logger.info(f"returning url_for('static', filename=f'images/icons/{icon_filename}')")
        return url_for('static', filename=f"images/icons/{icon_filename}")

    # If the icon doesn't exist, return a default icon URL
    app.logger.info("returning default icon url")
    return url_for('static', filename='images/icons/default-icon.png')
