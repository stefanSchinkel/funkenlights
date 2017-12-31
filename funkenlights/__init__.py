#!/usr/bin/env python
"""Flask factory."""
from flask import Flask

from . import views

def create_app(config):
    """Flask app factory."""

    app = Flask(__name__)
    app.register_blueprint(views.MAIN)
    app.config['binaries'] = config['binaries']
    app.config['devices'] = config['devices']
    app.run(host='0.0.0.0', debug=True)

    return app