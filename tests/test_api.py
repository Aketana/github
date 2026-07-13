from urllib import response

from app import app

client = app.test_client()

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.is_json
    assert response.json["status"] == "OK"
    assert response.json["version"] == "1.0"
    assert response.json["message"] == "Application is running"
    assert len(response.json) == 3

def test_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert response.is_json
    assert isinstance(response.json, list)

def test_get_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.is_json
    assert response.json["id"] == 1
    assert response.json["name"] == "Alice"
    assert response.json["job"] == "Engineer"

def test_get_user_not_found():
    response = client.get("/users/999")
    assert response.status_code == 404
    assert response.is_json
    assert response.json["error"] == "User not found"

def test_unknown_route():
    response = client.get("/unknown")
    assert response.status_code == 404

def test_hello():
    response = client.get("/hello/Aketana")
    assert "Hello Aketana" in response.get_data(as_text=True)

def test_user_count():
    response = client.get("/users")
    assert response.status_code == 200
    assert response.is_json
    assert response.json[0]["name"] == "Alice"
    assert response.json[1]["name"] == "Bob"

def test_create_user():
    response = client.post(
        "/users",
        json={
            "name": "David",
            "job": "Cloud Engineer"
        }
    )

    assert response.status_code == 201
    assert response.is_json
    assert "id" in response.json

def test_update_user():
    response = client.put(
        "/users/1",
        json={
            "name": "Alice Updated",
            "job": "Senior Engineer"
        }
    )

    assert response.status_code == 200
    assert response.is_json
    assert response.json["message"] == "User updated"

def test_delete_user():
    response = client.delete("/users/3")

    assert response.status_code == 200
    assert response.is_json
    assert response.json["message"] == "User deleted"

def test_delete_user_not_found():
    response = client.delete("/users/999")

    assert response.status_code == 404
    assert response.is_json
    assert response.json["error"] == "User not found"
