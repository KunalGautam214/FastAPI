from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_main_welcome():
    response = client.get('/welcome')
    assert response.json() == 'Welcome to FastAPI world'
