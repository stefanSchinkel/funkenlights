"""Tests for registration.
"""
import os
import json

from funkenlights.registrar import Registrar

#
# POST Tests
#
def test_no_payload(test_app):
    # Arange
    registrar = Registrar()
    data = {}
    # Act
    err_msg = 'This field is required.'
    with test_app.test_request_context(
        method="POST",
        data=json.dumps(data),
        content_type='application/json'):
        resp = registrar.post()
        data = json.loads(resp[0].data.decode())

    # Assert
    assert resp[1] == 422
    assert data['name'][0] == err_msg
    assert data['code_on'][0] == err_msg
    assert data['code_off'][0] == err_msg


def test_register_device(test_app):
    # Arange
    registrar = Registrar()
    empty = { "binaries": "foo", "devices": []}
    path = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(path, 'test.json'), 'w') as fp:
        json.dump(empty, fp)

    data = {
        "name": "foodevice",
        "code_on": 123,
        "code_off": 321
    }
    err_msg = 'This field is required.'

    # Act
    with test_app.test_request_context(
        method="POST",
        data=json.dumps(data),
        content_type='application/json'):
        resp = registrar.post()

    # Assert
    assert resp[1] == 200


