from models.book import Book

book1 = Book("The Colour of Magic", "Terry Pratchett", "Fantasy")
book1.checked_out = True
book2 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Science-Fiction")
book3 = Book("The Art of War", "Sun Tzu", "Treatise")

books = [book1, book2, book3]

class BookMethods:

    def add_book(books_list, book):
        books_list.append(book)

    def remove_book(books_list, book_index):
        del books_list[book_index]

    def check_in_book(books_list, book_index):
        books_list[book_index].checked_out = False

    def check_out_book(books_list, book_index):
        books_list[book_index].checked_out = True