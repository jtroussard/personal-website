# pylint: disable=multiple-imports,import-error,no-member,unused-variable,broad-exception-caught,invalid-name
"""
Module: routes
Description: Defines the routes and view functions for the Flask app.
"""

import os
import bleach

from flask import current_app as app
from flask import render_template
from flask import request
from flask import jsonify
from flask import make_response

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from personal_website.forms import HireMeForm
from personal_website.content.loaders import ContentLoader

@app.route("/")
@app.route("/home")
def home():
    """
    Route: Home page.
    :return: The home.html file is being returned.
    """
    content_loader = ContentLoader(app.config, app.logger)

    # Get content data object from CDN
    portfolio_data = content_loader.load_json("portfolio.json")
    social_data = content_loader.load_json("social.json")
    projects_data = content_loader.load_json("projects.json")

    # Check if data was retrieved
    if portfolio_data is None:
        app.logger.error("content loader did not deliver portfolio data")
    if social_data is None:
        app.logger.error("content loader did not deliver social data")
    if projects_data is None:
        app.logger.error("content loader did not deliver projects data")

    # Forms
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
            # SendGrids service to send mail to myself is a little wonky, so I have to move the contact detail fields into the message field.
            form.message.data = f"Name: {form.name.data}\nEmail: {form.email.data}\n\n{form.message.data}"
            # Sanitize the user-generated content before using it in HTML
            sanitized_message = bleach.clean(form.message.data, strip=True)

            # Just realized this could be configured somewhere else, created an issue for that.
            message = Mail(
                from_email=os.getenv("MAIL_DEFAULT_SENDER"),
                to_emails=os.getenv("MAIL_DEFAULT_SENDER"),
                subject="New Hire Me Form Submission",
                html_content=f"<strong>{sanitized_message}</strong>",
            )

            try:
                sg = SendGridAPIClient(os.environ.get("SENDGRID_API_KEY"))
                response = sg.send(message)
                app.logger.info(response.status_code)
                app.logger.info(response.body)
                response = {"message": "Form submitted successfully!"}
                resp = make_response(jsonify(response), 200)
                resp.headers["Strict-Transport-Security"] = "max-age=31536000"
                resp.headers["X-Frame-Options"] = "DENY"
                resp.headers["Content-Security-Policy"] = "default-src 'self';"
                resp.headers["X-Content-Type-Options"] = "nosniff"
                resp.headers["X-XSS-Protection"] = "1; mode=block"
                resp.headers["X-Content-Duration"] = "0"
                resp.headers["Expect-CT"] = "enforce, max-age=2592000"
                app.logger.info("------- HEADERS -------")
                for header in resp.headers:
                    app.logger.info(header)
                return resp
            except Exception as error:
                response = {"message": "Form submission failed!"}
                app.logger.error(error)
                return jsonify(response), 500
        else:
            return (
                jsonify({"message": "Form validation failed!", "errors": form.errors}),
                400,
            )
    else:
        return jsonify({"message": "Method not allowed!"}), 405

@app.context_processor
def inject_signed_urls():
    """
    Function: inject_signed_urls
    Description: Provides signed URLs. These are interpolated into the layout.html template.
    :return: A dictionary of signed URLs for CSS files.
    """
    content_loader = ContentLoader(app.config, app.logger)
    aos_css_url = content_loader.generate_signed_url("aos.css", "css")
    bootstrap_css_url = content_loader.generate_signed_url("bootstrap.min.css", "css")
    main_css_url = content_loader.generate_signed_url("main.css", "css")
    return {
        "aos_css_url": aos_css_url,
        "bootstrap_css_url": bootstrap_css_url,
        "main_css_url": main_css_url,
    }

@app.route("/weight-tracker", methods=["GET"])
def weight_tracker():
    """
    Route: Weight tracker flask application demo
    """
    return render_template("coming-soon.html")
