# pylint: disable=wrong-import-position, missing-module-docstring
from flask import Flask

from personal_website.config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config["SECRET_KEY"] = "this-is-a-super-secret-key-wubalubadubdub"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

# Avoid circular dependencies
from personal_website import routes