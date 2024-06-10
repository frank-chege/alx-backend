#!/usr/bin/env python3
from flask_babel import Babel
'''creating a flask app'''

app = __import__('0-app').app

class Config:
    '''configure the app'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    
    def __init__(self, app) -> None:
        app.config['BABEL_DEFAULT_LOCALE'] = self.BABEL_DEFAULT_LOCALE
        app.config['BABEL_SUPPORTED_LOCALES'] = self.LANGUAGES
        app.config['DEFAULT_TIMEZONE'] = self.DEFAULT_TIMEZONE

Config(app)
babel = Babel(app)

if __name__ == '__main__':
    app.run()