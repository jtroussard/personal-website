import os
from flask import url_for
from personal_website import app

def get_icon_url(input_string):
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
    app.logger.info(f"returning default icon url")
    return url_for('static', filename='images/default-icon.png')
