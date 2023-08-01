#!/usr/bin/env python3
"""
    First you will setup a basic Flask app in 0-app.py.
    Create a single / route and an index.html template
    that simply outputs “Welcome to Holberton” as page
    title (<title>) and “Hello world” as header (<h1>).
"""

from flask import Flask, render_template, request
from flask_babel import Babel
import pytz


app = Flask(__name__)
babel = Babel(app)


@app.before_request
def setTimeZone():
    """Sets the default timezone to UTC"""
    request.tzinfo = pytz.timezone("UTC")


@app.route('/')
def welcome():
    """Returns the index page"""
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run()
