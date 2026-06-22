from app import app


def test_index():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["app"] == "ecr-lab"
    assert data["message"] == "Hello from Flask Docker container v2"


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "ok"
    assert data["app"] == "ecr-lab"


def test_hello_name():
    client = app.test_client()

    response = client.get("/hello/Daniel")

    assert response.status_code == 200

    data = response.get_json()

    assert data["message"] == "Hello Daniel"
    assert data["app"] == "ecr-lab"
