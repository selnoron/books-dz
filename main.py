# Python
from typing import Any

# Flask
from flask import (
    Flask, 
    render_template,
)
from flask.app import Flask as FlaskApp

# Local
from models.book import *

app: FlaskApp = Flask(__name__)


@app.route("/home")
def home_page() -> str:
    return "Welcome to my first page!"

@app.route("/")
def main_page() -> str:
    return render_template(
        'index.html'
    )

@app.route("/num")
def get_nubmers() -> str:
    result: str = ""
    for i in range(1, 2001):
        result += f"<h2>{i}</h2>"

    return result

if __name__ == '__main__':

    app.run(
        port=8080,
        debug=True
    )