import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    res = client.get("/")
    assert res.status_code == 200
    assert b"Home Page" in res.data

def test_square(client):
    res = client.get("/square?num=3")
    assert res.status_code == 200
    assert b"The square of 3 is 9" in res.data

def test_add(client):
    res = client.get("/add?x=2&y=5")
    assert res.status_code == 200
    assert b"2 + 5 = 7" in res.data

def test_about(client):
    res = client.get("/about")
    assert res.status_code == 200
    assert b"About Page" in res.data
    assert b"generated at" in res.data