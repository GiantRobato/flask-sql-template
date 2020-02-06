import os
from flask import Flask, jsonify, render_template, request

def create_app() -> Flask:
    """ Flask app factory.

        Loads configuration for database connections, routes, secrets, etc.
    """
    app = Flask(__name__, instance_relative_config=False)

    with app.app_context():
        from .api import api

        app.register_blueprint(api, url_prefix="/api")

    return app
