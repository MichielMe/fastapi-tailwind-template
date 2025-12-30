# tests/test_main.py
from fastapi.testclient import TestClient


def test_read_main(client: TestClient):
    """
    Test that the root endpoint returns a 200 OK status.
    """
    response = client.get("/")
    assert response.status_code == 200

