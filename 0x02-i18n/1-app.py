#!/usr/bin/env python3
"""A module that defines a Flask App."""

from flask import Flask, render_template, request
from flask_babel import Babel
from typing import List


app = Flask(__name__)


class Config:
    """Defines the supported languages for translation.
    """
    LANGUAGES: List[str] = ["en", "fr"]


babel = Babel(app)


@babel.localeselector
def get_locale():
    """Returns the language to be translated into.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def home():
    """Gets the Home Page.
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
