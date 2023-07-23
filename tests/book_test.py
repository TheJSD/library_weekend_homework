import unittest
from models.book import Book
from models.book_list import BookMethods, book1, book2, book3

class TestBook(unittest.TestCase):

    def setUp(self):
        self.book1 = Book("The Colour of Magic", "Terry Pratchett", "Fantasy")
        self.book2 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Science-Fiction")
        self.book3 = Book("The Art of War", "Sun Tzu", "Treatise")
        self.books = [book1, book2, book3]
    
    def test_add_book(self):
        book4 = Book("Varieties of Daedra", "Aranea Drethan", "Fantasy")
        BookMethods.add_book(self.books, book4)
        number_of_books = len(self.books)
        self.assertEqual(4, number_of_books)
    
    def test_remove_book(self):
        BookMethods.remove_book(self.books, 0)
        number_of_books = len(self.books)
        self.assertEqual(2, number_of_books)

    def test_check_in_book(self):
        self.books[0].checked_out = True
        BookMethods.check_in_book(self.books, 0)
        self.assertEqual(False, self.books[0].checked_out)
    
    def test_check_out_book(self):
        BookMethods.check_out_book(self.books, 0)
        self.assertEqual(True, self.books[0].checked_out)