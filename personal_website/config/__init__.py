# pylint: disable=import-error, too-few-public-methods
"""
personal_website.config

This module defines the configuration classes for different environments:
- ProductionConfig
- DevelopmentConfig
- TestingConfig

It also loads environment variables from a .env file using dotenv.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    """
    Base configuration class.
    """
    DEBUG = os.getenv('DEBUG')
    TESTING = os.getenv('TESTING')
    CSRF_ENABLED = os.getenv('CSRF_ENABLED')
    SECRET_KEY = os.getenv('SECRET_KEY')

class ProductionConfig(Config):
    """
    Production configuration class.
    """
    DEBUG = False
    PORT = 8000

class DevelopmentConfig(Config):
    """
    Development configuration class.
    """
    DEVELOPMENT = True
    DEBUG = True
    PORT = 8000

class TestingConfig(Config):
    """
    Testing configuration class.
    """
    TESTING = True
    PORT = 8000
