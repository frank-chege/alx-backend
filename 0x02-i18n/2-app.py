#!/usr/bin/env python3
'''get the locale'''
from flask import request

app = __import__('1-app').app
def get_locale():
    '''gets the locale'''
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])