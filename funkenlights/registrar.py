"""Registrar - class to register devices
"""
from flask import jsonify
from flask.views import MethodView

from funkenlights import config as default_config
from funkenlights.core import _check_payload


class Registrar(MethodView):
    """This class is used to accept new devices Registrar"""
    def __init__(self, config=None):
        super(Registrar, self).__init__()
        if config:
            self.config = config
        else:
            self.config = default_config


    def get(self):
        """Render a template to input data."""
        return "config set to %s" % self.config.CFG

    def post(self):
        """Register a device"""
        _fields = ["name", "code_on", "code_off"]
        success, data = _check_payload(_fields)

        if not success:
            return jsonify(data), 422
