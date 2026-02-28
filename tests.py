from main import BooksCollector
import pytest
import random



class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
       
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize("book_name", [
        "А" * 40,
        "Книга с пробелами",
        "Книга-с-дефисом",
        "12345"
    ])
    def test_add_new_book_valid_names(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre


    def test_add_new_book_not_add_duplicate(self, collector):
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
    def test_set_book_genre_valid_genres_good_add(self, collector, book_name, genre, expected_genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == expected_genre


    def test_set_book_genre_invalid_genre_not_set(self, collector):
        book_name = "Книга1"
        genre = "Несуществующий жанр"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == ""
        

    def test_get_books_with_specific_genre_good_get(self, collector):
        books = ["Книга1", "Книга2", "Книга3", "Книга4", "Книга5"]
        genre = ['Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        for i, book in enumerate(books):
            collector.add_new_book(book)
            if i < 2:
                collector.set_book_genre(book,"Фантастика")
            else:
                random_genre = random.choice(genre)
                collector.set_book_genre(book,random_genre)
        
        assert collector.get_books_with_specific_genre("Фантастика") == ["Книга1", "Книга2"]


    def test_get_books_with_specific_genre_invalid_genre_not_add(self, collector, collector_with_books):
        assert collector.get_books_with_specific_genre("Invalid genre") == []



    def test_get_books_for_children_good_get(self, collector, collector_with_books ):
        assert collector.get_books_for_children() == ['Книга1', 'Книга4', 'Книга5']

    def test_add_book_in_favorites_adds_book(self, collector):
        book_name = "Книга в Избранном"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert collector.get_list_of_favorites_books() == ["Книга в Избранном"]

    def test_delete_book_from_favorites_removes_book_good_remove(self, collector):
        book_name = "Книга в Избранном для удаления"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert collector.get_list_of_favorites_books() == []


