# pylint: disable=wrong-import-position, missing-module-docstring
import os
from flask import Flask
# from personal_website.config import DevelopmentConfig

# Helper functions
def register_filters(app):
    from personal_website.filters import get_icon_url
    app.logger.info('registering filters')
    app.jinja_env.filters['get_icon_url'] = get_icon_url

app = Flask(__name__)
# app.config.from_object(DevelopmentConfig)

register_filters(app)

# Avoid circular dependencies
from personal_website import routes
