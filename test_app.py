import pytest
from app import app, local_analysis


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as test_client:
        yield test_client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


def test_analyze_without_json(client):
    response = client.post("/analyze")
    assert response.status_code == 415

def test_analyze_empty_situation(client):
    response = client.post(
        "/analyze",
        json={"situation": "   "}
    )
    assert response.status_code == 400


def test_high_risk_detection():
    result = local_analysis("Someone is following me")
    assert result["risk"] == "HIGH"


def test_medium_risk_detection():
    result = local_analysis("I feel unsafe")
    assert result["risk"] == "MEDIUM"


def test_low_risk_detection():
    result = local_analysis("I am studying at home")
    assert result["risk"] == "LOW"