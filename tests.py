from main import BooksCollector
import pytest
import random


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    @pytest.mark.parametrize("book_name", [
        "А" * 40,
        "Книга с пробелами",
        "Книга-с-дефисом",
        "12345"
    ])
    def test_add_new_book_valid_names(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre


    def test_add_new_book_duplicate(self):
        collector = BooksCollector()
        book_name = "Дубликат"
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == 1


    @pytest.mark.parametrize("book_name, genre, expected_genre", [
        ("Книга1", "Фантастика", "Фантастика"),
        ("Книга2", "Ужасы", "Ужасы"),
        ("Книга3", "Детективы", "Детективы"),
        ("Книга4", "Мультфильмы", "Мультфильмы"),
        ("Книга5", "Комедии", "Комедии"),
    ])
    def test_set_book_genre_valid_genres(self, book_name, genre, expected_genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == expected_genre


    def test_get_books_with_specific_genre(self):
        books = ["Книга1", "Книга2", "Книга3", "Книга4", "Книга5"]
        genre = ['Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        collector = BooksCollector()
        for i, book in enumerate(books):
            collector.add_new_book(book)
            if i < 2:
                collector.set_book_genre(book,"Фантастика")
            else:
                random_genre = random.choice(genre)
                collector.set_book_genre(book,random_genre)
        
        assert collector.get_books_with_specific_genre("Фантастика") == ["Книга1", "Книга2"]


    def test_get_books_for_children_success(self):
        books = ["Книга1", "Книга2", "Книга3", "Книга4", "Книга5"]
        genre = ['Фантастика','Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        collector = BooksCollector()
        for i, book in enumerate(books):
                collector.add_new_book(book)
                collector.set_book_genre(book, genre[i])

        assert collector.get_books_for_children() == ['Книга1', 'Книга4', 'Книга5']

    def test_add_book_in_favorites_adds_book(self):
        book_name = "Книга в Избранном"
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert collector.get_list_of_favorites_books() == ["Книга в Избранном"]

    def test_delete_book_from_favorites_removes_book(self):
        book_name = "Книга в Избранном для удаления"
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert collector.get_list_of_favorites_books() == []


