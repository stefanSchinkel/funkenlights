"""Registrar - class to register devices
"""
import json

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

        with open(self.config.CFG, mode="r", encoding="utf-8") as config:
            cfg = json.load(config)

        try:
            cfg["devices"]
        except KeyError:
            cfg["devices"] = []

        cfg["devices"].append(
            {
                "id": len(cfg["devices"]) + 1,
                "name": data["name"],
                "code_on": data["code_on"],
                "code_off": data["code_off"],
            }
        )

        with open(self.config.CFG, mode="w", encoding="utf-8") as config:
            json.dump(cfg, config, indent=4)

        return "", 200
