import unittest
from models.book import Book
from models.book_list import BookMethods, book1, book2, book3, books

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book1 = book1
        self.book2 = book2
        self.book3 = book3
        self.books = books
    
    def test_add_book(self):
        book4 = Book("Varieties of Daedra", "Aranea Drethan", "Fantasy")
        BookMethods.add_book(book4)
        number_of_books = len(self.books)
        self.assertEqual(4, number_of_books)
    
    def test_remove_book(self):
        
        number_of_books = len(self.books)
        self.assertEqual(4, number_of_books)