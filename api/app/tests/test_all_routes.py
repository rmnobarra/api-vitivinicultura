from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def get_auth_headers():
    login_data = {
        "username": "admin",
        "password": "1234"
    }
    response = client.post("/login", data=login_data)
    assert response.status_code == 200
    token = response.json().get("access_token")
    return {"Authorization": f"Bearer {token}"}

def test_producao():
    headers = get_auth_headers()
    response = client.get("/producao?ano=2023", headers=headers)
    assert response.status_code == 200
    assert "dados" in response.json()
    assert isinstance(response.json()["dados"], list)

def test_processamento():
    headers = get_auth_headers()
    response = client.get("/processamento?ano=2023", headers=headers)
    assert response.status_code == 200
    assert "dados" in response.json()
    assert isinstance(response.json()["dados"], list)

def test_comercializacao():
    headers = get_auth_headers()
    response = client.get("/comercializacao?ano=2023", headers=headers)
    assert response.status_code == 200
    assert "dados" in response.json()
    assert isinstance(response.json()["dados"], list)

def test_importacao():
    headers = get_auth_headers()
    response = client.get("/importacao?ano=2023", headers=headers)
    assert response.status_code == 200
    assert "dados" in response.json()
    assert isinstance(response.json()["dados"], list)

def test_exportacao():
    headers = get_auth_headers()
    response = client.get("/exportacao?ano=2023", headers=headers)
    assert response.status_code == 200
    assert "dados" in response.json()
    assert isinstance(response.json()["dados"], list)
