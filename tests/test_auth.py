from fastapi.testclient import TestClient
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from backend.app.main import app

client = TestClient(app)


def test_register_and_login():
    data = {"email": "user@example.com", "password": "secret"}
    r = client.post("/auth/register", json=data)
    assert r.status_code == 200

    form = {"username": data["email"], "password": data["password"]}
    r = client.post("/auth/login", data=form)
    assert r.status_code == 200
    assert "access_token" in r.json()
