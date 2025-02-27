import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import create_app

@pytest.fixture
def app():
    """
    Create and configure a new app instance for testing.
    """
    app, _ = create_app()
    app.config["TESTING"] = True
    app.config["DEBUG"] = True
    yield app

@pytest.fixture
def client(app):
    """
    Create a test client for Flask application.
    """
    return app.test_client()
