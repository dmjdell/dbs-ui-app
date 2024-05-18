import os
import pytest
from app import app  # Assuming your code is in 'app.py'

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello world" in response.data

@pytest.mark.parametrize("pod_name,expected_message", [
    ("test-pod-1", b"Hello world from test-pod-1"),
    ("test-pod-2", b"Hello world from test-pod-2")
])
def test_index_with_pod_name(client, monkeypatch, pod_name, expected_message):
    monkeypatch.setenv('MY_POD_NAME', pod_name)
    response = client.get('/')
    assert response.status_code == 200
    assert expected_message in response.data

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.data == b'OK'

def test_not_found(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404
