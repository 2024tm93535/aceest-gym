def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_add_member(client):
    payload = {
        "name": "John",
        "age": 25,
        "membership_end": "2026-12-31"
    }

    response = client.post("/members", json=payload)
    assert response.status_code == 201


def test_get_members(client):
    response = client.get("/members")
    assert response.status_code == 200


def test_bmi_calculation(client):
    payload = {
        "weight": 70,
        "height": 1.75
    }

    response = client.post("/bmi", json=payload)
    assert response.status_code == 200


def test_get_workouts(client):
    response = client.get("/workouts")
    assert response.status_code == 200


def test_expired_members(client):
    response = client.get("/membership/expired")
    assert response.status_code == 200