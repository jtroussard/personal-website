"""
Module: forms
Description: This module defines the HireMeForm class for handling contact form data.
"""

from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField
from wtforms import StringField, TextAreaField, EmailField
from wtforms.validators import InputRequired, Email

class HireMeForm(FlaskForm):
    """
    HireMeForm class is used to define the structure of the contact form.
    
    Attributes:
        name (StringField): Field for the user's name.
        email (EmailField): Field for the user's email.
        message (TextAreaField): Field for the user's message.
        recaptcha (RecaptchaField): Field for reCAPTCHA verification.
    """

    name = StringField('Name', render_kw={"placeholder": "Enter your name"}, validators=[InputRequired()])
    email = EmailField('Email', render_kw={"placeholder": "Enter your email"}, validators=[InputRequired(), Email()])
    message = TextAreaField('Message', render_kw={"placeholder": "Enter your message"}, validators=[InputRequired()])
    recaptcha = RecaptchaField()
