# pylint: skip-file
from flask import Flask
from .config import Config

# from personal_website.config import DevelopmentConfig


# Helper functions
def register_filters(flask_app):
    """
    Register custom Jinja2 filters.
    :param app: Flask application instance.
    """
    from personal_website.filters import get_icon_url

    flask_app.logger.info("registering filters")
    flask_app.jinja_env.filters["get_icon_url"] = get_icon_url
    flask_app.logger.info("registered get_icon_url")


def init_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():
        register_filters(app)

        from . import routes

        return app
