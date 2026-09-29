# tests/test_app.py
from app import app


def test_hello_world_returns_200():
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert b"Hello" in response.data


def test_checksum_endpoint_exists():
    with app.test_client() as client:
        response = client.get("/checksum?data=abc")
        assert response.status_code == 200
