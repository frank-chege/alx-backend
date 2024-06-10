#!/usr/bin/env python3
from flask_babel import Babel
'''creating a flask app'''

app = __import__('0-app').app

class Config:
    '''configure the app'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    DEFAULT_TIMEZONE = 'UTC'
    
Config(app)
babel = Babel(app)

if __name__ == '__main__':
    app.run()