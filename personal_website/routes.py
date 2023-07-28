# pylint: disable=multiple-imports, import-error
"""
personal_website.routes

This module defines the routes and view functions for the Flask app.

Routes:
- / and /home: Renders the home page with portfolio data from a JSON file.
- /weight-tracker: Renders the "coming-soon" page for the weight tracker demo.
"""
import os, json
from flask import render_template
from personal_website import app

@app.route("/")
@app.route("/home")
def home():
    """
    Route: Home page.
    :return: The home.html file is being returned.
    """
    # Read the path to the JSON file from the environment variable
    data_path = os.environ.get('PORTFOLIO_DATA_PATH')
    print(data_path)

    if data_path is None:
        return "Error: Portfolio data path not set."

    # Load the JSON data from the file
    with open(data_path, 'r', encoding='utf-8') as json_file:
        portfolio_data = json.load(json_file)
    return render_template("home.html", active_page="home", data=portfolio_data)

@app.route("/weight-tracker", methods=["GET"])
def weight_tracker():
    """
    Route: Weight tracker flask application demo
    """
    return render_template("coming-soon.html")
