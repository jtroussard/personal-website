# pylint: disable=wrong-import-position, missing-module-docstring, import-outside-toplevel, import-error
from flask import Flask
# from personal_website.config import DevelopmentConfig

# Helper functions
def register_filters(flask_app):
    """
    Register custom Jinja2 filters.
    :param app: Flask application instance.
    """
    from personal_website.filters import get_icon_url
    flask_app.logger.info('registering filters')
    flask_app.jinja_env.filters['get_icon_url'] = get_icon_url

app = Flask(__name__)
# app.config.from_object(DevelopmentConfig)

register_filters(app)

# Avoid circular dependencies
from personal_website import routes
