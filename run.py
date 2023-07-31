"""
personal_website.run_app

This module runs the Flask application.

It imports the Flask app from personal_website package and starts the
development server if the script is executed directly.
"""
from personal_website import app

if __name__ == "__main__":
    app.run(port=12121, debug=True)
