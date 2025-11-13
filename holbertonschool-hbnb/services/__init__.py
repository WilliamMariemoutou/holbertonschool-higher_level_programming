#!/usr/bin/python3

"""
App Initialization
------------------
This module initializes the Flask application, sets up Flask-RESTx, and registers
the namespaces for different resources.
"""

from flask import Flask
from flask_restx import Api
from api.v1.amenities import api as amenities_ns

def create_app():
    """function to create and configure the Flask app."""
    app = Flask(__name__)

    api = Api(
        app,
        version='1.0',
        title='HBnB REST API',
        description='API documentation for the HBnB project.'
    )

    # Register the Amenity Namespace
    api.add_namespace(amenities_ns, path='/api/v1/amenities')

    return app
