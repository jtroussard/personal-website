# pylint: disable=multiple-imports,import-error,no-member
"""
personal_website.routes

This module defines the routes and view functions for the Flask app.

Routes:
- / and /home: Renders the home page with portfolio data from a JSON file.
- /hire-me: Handles the submission of the "Hire Me" form.
- /weight-tracker: Renders the "coming-soon" page for the weight tracker demo.
"""
import os
import json
from flask import current_app as app
from flask import render_template, request, jsonify

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from personal_website.forms import HireMeForm


@app.route("/")
@app.route("/home")
def home():
    """
    Route: Home page.
    :return: The home.html file is being returned.
    """
    # Read the path to the JSON file from the environment variable
    portfolio_data_path = os.environ.get(
        "PORTFOLIO_DATA_PATH", "personal_website/content_files/portfolio.json"
    )
    social_data_path = os.environ.get(
        "SOCIAL_DATA_PATH", "personal_website/content_files/social.json"
    )
    projects_data_path = os.environ.get(
        "PROJECTS_DATA_PATH", "personal_website/content_files/projects.json"
    )

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

    form = HireMeForm()
    return render_template(
        "home.html",
        active_page="home",
        portfolio=portfolio_data,
        social=social_data,
        projects=projects_data,
        title="Jacques Troussard",
        form=form,
    )


@app.route("/hire-me", methods=["POST"])
def hire_me():
    """
    Route: Handles the submission of the "Hire Me" form.
    :return: JSON response indicating the status of the form submission.
    """
    form = HireMeForm(request.form)
    if request.method == "POST":
        if form.validate_on_submit():
            message = Mail(
                from_email=os.getenv("DEFAULT_MAIL_SENDER"),
                to_emails=os.getenv("DEFAULT_MAIL_SENDER"),
                subject="New Hire Me Form Submission",
                html_content=f"<strong>{form.message.data}</strong>",
            )

            try:
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY')) # pylint: disable=invalid-name
                response = sg.send(message)
                app.logger.info(response.status_code)
                app.logger.info(response.body)
                app.logger.info(response.headers)
                response = {"message": "Form submitted successfully!"}
                return jsonify(response), 200
            except Exception as error: # pylint: disable=unused-variable, broad-exception-caught
                response = {"message": "Form submission failed!"}
                return jsonify(response), 500
        else:
            return (
                jsonify({"message": "Form validation failed!", "errors": form.errors}),
                400,
            )
    else:
        return jsonify({"message": "Method not allowed!"}), 405


@app.route("/weight-tracker", methods=["GET"])
def weight_tracker():
    """
    Route: Weight tracker flask application demo
    """
    return render_template("coming-soon.html")
