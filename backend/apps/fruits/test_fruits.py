from fastapi.testclient import TestClient
from main import (
    app,
)  

client = TestClient(app)


def test_create_fruit(setup_db):
    response = client.post("/fruits", json={"name": "Lemon", "category_id": 1})
    assert response.status_code == 200
    assert response.json()["name"] == "Lemon"
    assert response.json()["category"]["name"] == "Citrus"


def test_get_fruits(setup_db):
    response = client.get("/fruits")
    assert response.status_code == 200
    fruits = response.json()
    assert len(fruits) > 0
    assert fruits[0]["name"] == "Orange"


def test_get_fruit_by_id(setup_db):
    response = client.get("/fruits/1")
    assert response.status_code == 200
    fruit = response.json()
    assert fruit["name"] == "Orange"
    assert fruit["category"]["name"] == "Citrus"


def test_update_fruit(setup_db):
    response = client.put("/fruits/1", json={"name": "Mandarin", "category_id": 1})
    assert response.status_code == 200
    assert response.json()["name"] == "Mandarin"


def test_delete_fruit(setup_db):
    response = client.delete("/fruits/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Orange"
