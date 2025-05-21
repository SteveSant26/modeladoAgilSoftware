from fastapi.testclient import TestClient

from main import (
    app,
)


client = TestClient(app)


def test_create_category(setup_db):
    response = client.post("/categories", json={"name": "Electrónica"})
    assert response.status_code == 200
    assert response.json()["name"] == "Electrónica"


def test_get_categories(setup_db):
    response = client.get("/categories")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_category_by_id(setup_db):
    response = client.get("/categories/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Electrónica"


def test_update_category(setup_db):
    response = client.put("/categories/1", json={"name": "Hardware"})
    assert response.status_code == 200
    assert response.json()["name"] == "Hardware"


def test_delete_category(setup_db):
    response = client.delete("/categories/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Category deleted successfully"


def test_get_category_not_found(setup_db):
    response = client.get("/categories/999") 
    assert response.status_code == 404
    assert response.json()["detail"] == "Category not found"
