"""Abtraction layer for testing in flask.

Provide an Abstract class from which everything inherits which
provides a common entry point for test configurations.
"""

from flask_testing import TestCase

from funkenlights import create_app
from funkenlights import config


class AbstractBaseTest(TestCase):
    """AbstractBase provides setup/teardown and create_app."""

    def create_app(self):
        """Use factory to instantiate test app.

        This is required by TestCase and will expose
        the Flask app and the Werkzeug client for testing as follows:
        self.app = self.create_app()
        self.client = self.app.test_client()"""
        app = create_app(config)
        app.config['TESTING'] = True
        return app