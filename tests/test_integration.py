from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_valid_name_in_api_returns_with_age_field_in_response():
    body = {"name": "test"}

    response = client.post("/api/human-age", json=body)
    assert response.status_code == 200
    assert "age" in response.json()

def test_invalid_name_in_api_returns_with_bad_request():
    body = {"name": "xttrfgfbfbgfbfbfbgf"}

    response = client.post("/api/human-age", json=body)
    assert response.status_code == 400

