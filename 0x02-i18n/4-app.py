#!/usr/bin/env python3
'''get the locale'''
from flask import request, render_template, Flask
from flask_babel import Babel

get_locale = __import__('3-app').get_locale

def check_locale(get_locale):
    def wrapper():
        locale = request.args.get('locale')
        if locale == 'fr':
            return 'fr'
        else:
            return request.accept_languages.best_match(app.config['LANGUAGES'])
    return wrapper

get_locale = check_locale(get_locale)