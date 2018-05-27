#!/usr/bin/env python
"""Flask factory."""
import os
import json

from flask import Flask

from .registrar import Registrar

def create_app(config):
    """Flask app factory."""
    with open(config.CFG) as fp:
        cfg = json.load(fp)

    app = Flask(__name__)
    app.config['binaries'] = cfg['binaries']
    app.config['devices'] = cfg['devices']

    reg_view = Registrar.as_view('register')
    app.add_url_rule(
        '/register/',
        view_func=reg_view,
        methods=['GET', 'POST'])

    return app