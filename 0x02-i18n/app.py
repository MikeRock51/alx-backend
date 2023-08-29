#!/usr/bin/env python3
"""
    First you will setup a basic Flask app in 0-app.py.
    Create a single / route and an index.html template
    that simply outputs “Welcome to Holberton” as page
    title (<title>) and “Hello world” as header (<h1>).
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, get_locale
from typing import Dict
import pytz
from datetime import datetime


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configuration for the application"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Dict:
    """Returns the user with the id or None"""
    try:
        id = int(request.args.get('login_as'))
    except Exception:
        return None

    if id and id in users:
        return users[id]

    return None


@app.before_request
def before_request():
    """Finds a user, if any"""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """Determines the language to use"""
    locale = request.args.get('locale')
    if locale:
        if locale in app.config['LANGUAGES']:
            return request.args.get('locale')
    elif g.user:
        if g.user.get('locale') in app.config['LANGUAGES']:
            return g.user['locale']

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Determines the timezone to use"""
    timezone = request.args.get('timezone')
    if timezone and timezone in pytz.all_timezones:
        return timezone
    elif g.user:
        timezone = g.user.get('timezone')
        if timezone in pytz.all_timezones:
            return g.user['timezone']

    return 'UTC'


@app.route('/')
def welcome():
    """Returns the index page"""
    timezone = pytz.timezone(get_timezone())
    fmt = '%b %d, %Y, %I:%M:%S %p'
    g.current_time = datetime.now(timezone).strftime(fmt)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)