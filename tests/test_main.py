import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.services.events import events

client = TestClient(app)

@pytest.fixture(autouse=True)
def clear_events():
    events.clear()
    yield
    events.clear()

def test_day_of_week():
    response = client.get("/day-of-week?input_date=2026-10-11")

    assert response.status_code == 200
    assert response.json()["day_of_week"] == "Sunday"


def test_day_of_week_invalid_date():
    response = client.get("/day-of-week?input_date=hello")

    assert response.status_code == 422


def test_create_event():
    response = client.post(
        "/events",
        json={
            "name": "Vacation",
            "event_date": "2026-12-20",
        },
    )

    assert response.status_code == 201
    assert response.json()["name"] == "Vacation"
    assert response.json()["event_date"] == "2026-12-20"