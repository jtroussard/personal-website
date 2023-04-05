# pylint: disable=wrong-import-position, missing-module-docstring
from flask import Flask
from config import ProductionConfig

app = Flask(__name__)
app.config.from_object(ProductionConfig)

# Avoid circular dependencies
from personal_website import routes