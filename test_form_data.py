from fastapi.testclient import TestClient

from form_data import app

client = TestClient(app)


def test_user():
    payload = {
        'username': 'Code with KG',
        'password': 'password'
    }
    response = client.post('/user/form-data', data=payload)
    assert response.status_code == 200
    assert response.json() == {'username': {'username': 'Code with KG', 'password': 'password'}}


def test_create_user():
    payload = {
        'username': 'Code with KG'
    }
    response = client.post('/user', data=payload)
    assert response.status_code == 200
    assert response.json() == {'username': 'Code with KG'}
