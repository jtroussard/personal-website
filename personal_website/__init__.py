# pylint: skip-file
from flask import Flask
from flask_mail import Mail
from .config import Config
# from personal_website.config import DevelopmentConfig

# Helper functions
def setup_mail(flask_app):
    """
    Set up Flask-Mail.
    :param app: Flask application instance.
    """
    flask_app.logger.info('registering extensions')
    mail = Mail(flask_app)
    return mail

def register_filters(flask_app):
    """
    Register custom Jinja2 filters.
    :param app: Flask application instance.
    """
    from personal_website.filters import get_icon_url
    flask_app.logger.info('registering filters')
    flask_app.jinja_env.filters['get_icon_url'] = get_icon_url

def init_app():
    app = Flask(__name__)
    print(Config.ENVIRONMENT)
    app.config.from_object(Config)
    # print(app.config)

    with app.app_context():
        print(app.config)
        mail = setup_mail(app)
        register_filters(app)

        from . import routes

        return app
