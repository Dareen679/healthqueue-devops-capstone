import pytest
from app.main import app, appointments

@pytest.fixture
def client():
    app.config['TESTING'] = True
    appointments.clear()
    with app.test_client() as c:
        yield c

def test_health(client):
    assert client.get('/healthz').json['status'] == 'ok'

def test_ready(client):
    assert client.get('/readyz').status_code == 200

def test_invalid_body(client):
    assert client.post('/appointments', json={}).status_code == 400

def test_create_and_list(client):
    response = client.post('/appointments', json={'patient_ref': 'synthetic-001', 'starts_at': '2026-11-04T15:00:00Z'})
    assert response.status_code == 201
    assert len(client.get('/appointments').json['appointments']) == 1

def test_timezone_required(client):
    response = client.post('/appointments', json={'patient_ref': 'synthetic-001', 'starts_at': '2026-11-04T15:00:00'})
    assert response.status_code == 400
