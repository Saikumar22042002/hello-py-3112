import pytest
from app import app as flask_app

@pytest.fixture
def client():
    """Configures the app for testing and provides a test client."""
    flask_app.config['TESTING'] = True
    with flask_app.test_client() as client:
        yield client

def test_index_endpoint(client):
    """Tests the main '/' endpoint for status code and content."""
    response = client.get('/')
    assert response.status_code == 200
    expected_json = {
        "message": "Hello World",
        "repo": "Hello-py-3112",
        "branch": "hello-v1"
    }
    assert response.json == expected_json

def test_health_endpoint(client):
    """Tests the '/health' endpoint for a healthy status."""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {"status": "healthy"}
