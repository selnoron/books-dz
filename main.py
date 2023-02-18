# Python
from typing import Any

# Flask
from flask import (
    Flask, 
    render_template,
)
from flask.app import \
    Flask as FlaskApp

# Local
from models.book import *

app: FlaskApp = Flask(__name__)

#gennres of books
proza: list[dict] = []
fantazy: list[dict] = []
adventure: list[dict] = []
horror: list[dict] = []
biography: list[dict] = []
biblia: list[dict] = []

@app.route("/biblia")
def bib_page() -> FlaskApp:
    return render_template(
        'biblia.html',
        books=biblia
    )


@app.route("/biography")
def bio_page() -> FlaskApp:
    return render_template(
        'biography.html',
        books=biography
    )

@app.route("/horror")
def hor_page() -> FlaskApp:
    return render_template(
        'horror.html',
        books=horror
    )

@app.route("/adventure")
def adv_page() -> FlaskApp:
    return render_template(
        'adventure.html',
        books=adventure
    )

@app.route("/fantazy")
def fan_page() -> FlaskApp:
    return render_template(
        'fantazy.html',
        books=fantazy
    )

@app.route("/proza")
def proza_page() -> FlaskApp:
    return render_template(
        'proza.html',
        books=proza
    )

@app.route("/<id>")
def book_page(id: str) -> FlaskApp:
    return render_template(
        'book.html',
        book=books_json[int(id)]
    )

@app.route("/")
def main_page() -> FlaskApp:
    return render_template(
        'index.html',
        books=books_json
    )

if __name__ == '__main__':
    #sorting genres
    for book in books_json:
        if book.get("genre") == "Proza":
            proza.append(book)
        if book.get("genre") == "Fantazy":
            fantazy.append(book)
        if book.get("genre") == "Horror":
            horror.append(book)
        if book.get("genre") == "Biography":
            biography.append(book)
        if book.get("genre") == "Biblia":
            biblia.append(book)
        if book.get("genre") == "Adventure":
            adventure.append(book)

    app.run(
        port=8080,
        debug=True
    )
