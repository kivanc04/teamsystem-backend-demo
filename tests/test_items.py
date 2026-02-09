from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_create_and_get_item():
    create = client.post("/items", json={"name": "coffee", "price": 12.5})
    assert create.status_code == 201
    body = create.json()
    assert body["id"] >= 1
    assert body["name"] == "coffee"
    assert body["price"] == 12.5

    item_id = body["id"]
    getr = client.get(f"/items/{item_id}")
    assert getr.status_code == 200
    assert getr.json() == body


def test_get_missing_item_returns_404():
    r = client.get("/items/999999")
    assert r.status_code == 404
    assert r.json()["detail"] == "Item not found"
