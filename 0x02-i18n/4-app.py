#!/usr/bin/env python3
"""
    First you will setup a basic Flask app in 0-app.py.
    Create a single / route and an index.html template
    that simply outputs “Welcome to Holberton” as page
    title (<title>) and “Hello world” as header (<h1>).
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, get_locale


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configuration for the application"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Determines the best language match to use"""
    locale = request.args.get('locale')
    if locale:
        if locale in app.config['LANGUAGES']:
            return request.args.get('locale')

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def welcome():
    """Returns the index page"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(debug=True)
