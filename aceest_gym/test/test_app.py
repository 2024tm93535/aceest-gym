import pytest
from aceest_gym.app.app import create_app


@pytest.fixture
def client():

    app = create_app()

    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home(client):

    response = client.get("/")

    assert response.status_code == 200


def test_add_member(client):

    response = client.post("/members", json={
        "name": "Alice",
        "age": 24,
        "weight": 60,
        "membership": "Gold",
        "height":"1.5"
    })

    assert response.status_code == 200

def test_bmi(client):

    response = client.post("/bmi", json={
        "weight": 70,
        "height": 1.75
    })

    assert response.status_code == 200