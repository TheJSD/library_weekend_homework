from flask import render_template, Blueprint, request
from models.book_list import books, BookMethods
from models.book import Book

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/library")
def index():
    return render_template("index.jinja", title="Library Catalog", books=books)

@books_blueprint.route("/library/<index>")
def book(index):
    book = books[int(index) - 1]
    book_index = index
    return render_template("book.jinja", title=book.title, book=book, book_index=book_index)

@books_blueprint.route("/library/add_a_book")
def add_a_book_site():
    return render_template("/add_a_book.jinja", title="Add a Book")

@books_blueprint.route("/library", methods=["post"])
def add_a_book():
    new_book = Book(request.form["title"], request.form["author"], request.form["genre"])
    BookMethods.add_book(books, new_book)
    return render_template("index.jinja", title="Library Catalog", books=books)

@books_blueprint.route("/library/<index>/delete", methods=["post"])
def remove_book_from_library(index):
    BookMethods.remove_book(books, (int(index) - 1))
    return render_template("index.jinja", title="Library Catalog", books=books)

@books_blueprint.route("/library/<index>/check_out_toggle", methods=["post"])
def check_out_toggle(index):
    book = books[int(index) - 1]
    book_id = int(index)
    is_checked_out = request.form.get("check_out")
    if is_checked_out == "Check out":
        BookMethods.check_out_book(books, book_id - 1)
    else:
        BookMethods.check_in_book(books, book_id - 1)
    return render_template("book.jinja", title=book.title, book=book, book_index=book_id)
