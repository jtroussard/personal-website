# pylint: disable=no-member
"""
personal_website.run_app

This module runs the Flask application.

It imports the Flask app from personal_website package and starts the
development server if the script is executed directly.
"""
from personal_website import init_app

app = init_app()
host = app.config["HOST"]
port = app.config["PORT"]
app.logger.info(f"host: {host} and port: {port}")

if __name__ == "__main__":
    app.run(host=host, port=port)
