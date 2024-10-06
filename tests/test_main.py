from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI with PostgreSQL and HashiCorp Vault!"}

def test_login():
    response = client.post("/token", data={"username": "testuser", "password": "testpassword"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_protected_route():
    response = client.get("/protected", headers={"Authorization": "Bearer your_valid_token"})
    assert response.status_code == 200
    assert "message" in response.json()
    assert "current_user" in response.json()
