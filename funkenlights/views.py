from flask import Blueprint, render_template, jsonify
from flask import current_app as app

MAIN = Blueprint('route', __name__)

@MAIN.route('/')
def index():
    """Main status page."""
    return render_template('main.html', devices=app.config['devices'])

@MAIN.route('/success')
def success():
    """A 200 page"""
    return jsonify({"message": "success"})

@MAIN.route('/failure')
def failure():
    """A 400 page"""
    return jsonify({"message": "failure"}), 400