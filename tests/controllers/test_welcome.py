from expanse.testing.client import TestClient


def test_welcome(client: TestClient) -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "text/html; charset=utf-8"
