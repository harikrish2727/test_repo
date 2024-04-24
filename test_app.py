from app import app
from pytest import fixture

@fixture
def client():
    with app.test_client() as client:
        return client
    
def test_home_page(client):
    response = client.get("/home")
    assert response.status_code == 200
    assert response.text == "Home page"

def test_ping(client):
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.text == "Hello I am working"