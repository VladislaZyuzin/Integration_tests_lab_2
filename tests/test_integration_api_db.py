import json 
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_all_books(client):
    response = client.get("/api/v2/resources/books/all")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert all("title" in book for book in data)

def test_get_books_by_author(client):
    """Тест фильтрации по автору"""
    response = client.get("/api/v2/resources/books?author=Connie+Willis")
    assert response.status_code == 200
    data = response.get_json()
    assert all(book["author"] == "Connie Willis" for book in data)

def test_get_books_by_year(client):
    """Тест фильтрации по году издания"""
    response = client.get("/api/v2/resources/books?published=2010")
    assert response.status_code == 200
    data = response.get_json()
    assert all(book["published"] == 2010 for book in data)

def test_get_book_not_found(client):
    """Тест, когда книги не найдены"""
    response = client.get("/api/v2/resources/books?author=Nonexistent+Author")
    assert response.status_code == 200
    data = response.get_json()
    assert data == []  # должен вернуть пустой список

def test_invalid_endpoint(client):
    """Тест обращения к несуществующему маршруту"""
    response = client.get("/api/v2/resources/invalid")
    assert response.status_code == 404
