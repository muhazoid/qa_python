import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    """
    Базовая фикстура: создает новый экземпляр коллектора для каждого теста.
    Гарантирует изоляцию тестов.
    """
    return BooksCollector()

@pytest.fixture
def collector_with_books(collector):
    
    books_data = {
        "Книга1": "Фантастика",
        "Книга2": "Ужасы",
        "Книга3": "Детективы",
        "Книга4": "Мультфильмы",
        "Книга5": "Комедии"
    }
    
    for book, genre in books_data.items():
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        
    return collector