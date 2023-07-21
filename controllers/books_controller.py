from flask import render_template, Blueprint
from models.book_list import books

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/library")
def index():
    return render_template("index.jinja", title="Library Catalog", books=books)

@books_blueprint.route("/library/<index>")
def book(index):
    book = books[int(index) - 1]
    return render_template("book.jinja", title="{book.title}", book=book)