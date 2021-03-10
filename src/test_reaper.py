from fastapi.testclient import TestClient # Use the command to start unit tests: pytest --maxfail=2 --tb=line
from reaperserv import app
import requests 

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200 # Does a Status Code Check 