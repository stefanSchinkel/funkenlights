"""Tests for registration.
"""
import json

from .base import AbstractBaseTest
from funkenlights.registrar import Registrar


class BasicDeviceRegistrationTests(AbstractBaseTest):
    """RepoFactoryFailure -
    """

    @classmethod
    def setUpClass(cls):
        cls.registrar = Registrar()

    def test_no_payload(self):
        # Arange
        data = {}
        err_msg = 'This field is required.'
        with self.app.test_request_context(
            method="POST",
            data=json.dumps(data),
            content_type='application/json'):
            # Act
            response = self.registrar.post()
            data = json.loads(response[0].data.decode())

            # Assert
            self.assertEqual(response[1], 422)
            self.assertEqual(data['name'][0], err_msg)
            self.assertEqual(data['code_on'][0], err_msg)
            self.assertEqual(data['code_off'][0], err_msg)

