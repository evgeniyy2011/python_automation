import requests
import pytest

MY_URL = "http://127.0.0.1:8080"

def test_post_request():
    with open("sunflower.jpg", "rb") as f:
        response = requests.post(f"{MY_URL}/upload", files={"image":f})
        print(response.status_code)
        print(response.json())
        assert response.status_code == 201

def test_get_request():
    response = requests.get(f"{MY_URL}/image/sunflower.jpg", headers={"Content-Type" : "text"})
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200

def test_delete():
    response = requests.delete(f"{MY_URL}/delete/sunflower.jpg")
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200


