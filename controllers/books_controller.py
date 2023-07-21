from flask import render_template, Blueprint
from models.book_list import books

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/library")
def index():
    return render_template("index.jinja", title="Library Catalog", books=books)
