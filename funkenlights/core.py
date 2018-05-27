"""Core.py - common BL module."""
from flask import request

def _check_payload(fields):
    """Make sure the JSON payload is properly formed.
    """
    data = {}
    err = {}
    for item in fields:
        try:
            data[item] = request.json[item]
        # TypeError is needed in case _no_ JSON data was sent.
        except (KeyError, TypeError):
            err[item] = ["This field is required."]

    if not bool(err):
        return True, data

    return False, err