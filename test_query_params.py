from fastapi.testclient import TestClient

from query_params import app

client = TestClient(app)


def test_items():
    x = [i for i in range(10, 21)]
    response = client.get('/items/123?page=10&size=100')
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {'items': x, 'page': 10, 'size': 100}
