"""Fixtures to be used across tests
"""
import pytest

from funkenlights import config
from funkenlights import create_app

@pytest.fixture
def test_app():
    """Use factory to instantiate test app and return an app
    This can be injected to the tests (it has an app context)
    """
    app = create_app(config)
    app.config['TESTING'] = True
    return app