from fastapi.testclient import TestClient

from body_params import app

client = TestClient(app)


def test_body_parameters():
    payload = {
        'name': 'Code with KG',
        'description': 'Youtube tutorial channel',
        'price': 0.0,
        'tax': 0.0
    }
    response = client.post('/items', json=payload)
    assert response.status_code == 200
    assert response.json() == {
        'name': 'Code with KG',
        'description': 'Youtube tutorial channel',
        'price': 0.0,
        'tax': 0.0
    }
