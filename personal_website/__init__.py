# pylint: disable=wrong-import-position, missing-module-docstring
from flask import Flask

app = Flask(__name__)

# Avoid circular dependencies
from personal_website import routes