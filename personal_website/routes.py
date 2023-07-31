# pylint: disable=multiple-imports, import-error, no-member
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
    portfolio_data_path = os.environ.get("PORTFOLIO_DATA_PATH")
    social_data_path = os.environ.get("SOCIAL_DATA_PATH")
    projects_data_path = os.environ.get("PROJECTS_DATA_PATH")

    if portfolio_data_path is None:
        app.logger.error("Portfolio data path not set.")
    if social_data_path is None:
        app.logger.error("Social data path not set.")
    if projects_data_path is None:
        app.logger.error("Projects data path not set.")

    # Load the JSON data from the file
    with open(portfolio_data_path, "r", encoding="utf-8") as profilio_file, open(
        social_data_path, "r", encoding="utf-8"
    ) as social_file, open(projects_data_path, "r", encoding="utf-8") as projects_file:
        portfolio_data = json.load(profilio_file)
        social_data = json.load(social_file)
        projects_data = json.load(projects_file)
    return render_template(
        "home.html",
        active_page="home",
        portfolio=portfolio_data,
        social=social_data,
        projects=projects_data,
        title="Jacques Troussard",
    )

@app.route("/weight-tracker", methods=["GET"])
def weight_tracker():
    """
    Route: Weight tracker flask application demo
    """
    return render_template("coming-soon.html")
