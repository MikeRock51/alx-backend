#!/usr/bin/env python3
"""Sets up the prerequisite for the application"""

from flask import request


@babel.localeselector
def get_locale():
    """Sets the default locale language to english"""
    return 'en'
