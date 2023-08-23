# pylint: disable=too-few-public-methods
"""Flask App configuration."""
from os import environ, path
from dotenv import load_dotenv

program_env = environ.get("PROGRAM_ENV", "development")
location_env = environ.get("LOCATION_ENV", path.dirname(__file__))
dotenv_path = path.join(f"{location_env}", f"{program_env}.env")
load_dotenv(dotenv_path=dotenv_path)


class Config:
    """Set Flask config variables."""

    # General Config
    ENVIRONMENT = environ.get("ENVIRONMENT", "development")
    FLASK_APP = environ.get("FLASK_APP", "app")
    DEBUG = environ.get("DEBUG", "true")
    SECRET_KEY = environ.get("SECRET_KEY", "1234567890987654321")
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"
    HOST = environ.get("HOST", "localhost")
    PORT = environ.get("PORT", "12031")
    RECAPTCHA_PUBLIC_KEY = environ.get("RECAPTCHA_PUBLIC_KEY", "1234567890987654321")
    RECAPTCHA_PRIVATE_KEY = environ.get("RECAPTCHA_PRIVATE_KEY", "1234567890987654321")
    SENDGRID_API_KEY = environ.get("SENDGRID_API_KEY", "1234567890987654321")
    MAIL_DEFAULT_SENDER = environ.get("MAIL_DEFAULT_SENDER", "your_email@example.com")
    BUCKET_NAME = environ.get("BUCKET_NAME", "I am bucket head man!")
    KAGIS = environ.get("KAGIS", "I am the kangaroo!")

    # Conditionals
    # SERVER_NAME causes some issues during local development, but is required for
    # url_for() to work properly in production.
    if ENVIRONMENT == "development":
        SERVER_NAME = None
    else:
        SERVER_NAME = environ.get("SERVER_NAME", "localhost:12031")

    def __repr__(self) -> str:
        return f"<Config:\n  ENVIRONMENT: {self.ENVIRONMENT}\n  FLASK_APP: \
            {self.FLASK_APP}\n  DEBUG: {self.DEBUG}\n  SECRET_KEY: \
                {self.SECRET_KEY}\n  HOST: {self.HOST}\n  PORT: {self.PORT}\n>"
