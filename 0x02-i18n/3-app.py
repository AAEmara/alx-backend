#!/usr/bin/env python3
"""A module that defines a Flask App."""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext
from typing import List


app = Flask(__name__)


class Config:
    """Defines the supported languages for translation.
    """
    LANGUAGES: List[str] = ["en", "fr"]


app.config.from_object(Config)
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
    home_title: str = gettext(u'Welcome to Holberton')
    home_header: str = gettext(u'Hello world!')
    return render_template("3-index.html",
                           home_title=home_title,
                           home_header=home_header)


if __name__ == "__main__":
    app.run(debug=True)
