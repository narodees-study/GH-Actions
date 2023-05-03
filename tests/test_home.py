import requests


def test_home_route():
    response = requests.get('http://localhost:8080/')
    data = response.json()
    assert response.status_code == 200
    assert data['status'] == 'ok'
