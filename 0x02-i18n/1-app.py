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


app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def home():
    """Gets the Home Page.
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
