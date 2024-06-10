#!/usr/bin/env python3
import importlib
from flask_babel import Babel

# Dynamically import the Flask app from the module 0-app
module_name = '0-app'
app_module = importlib.import_module(module_name)
app = app_module.app

class Config:
    '''configure the app'''
    LANGUAGES = ["en", "fr"]

    @staticmethod
    def init_app(app):
        app.config['BABEL_DEFAULT_LOCALE'] = 'en'
        app.config['BABEL_SUPPORTED_LOCALES'] = Config.LANGUAGES
        app.config['DEFAULT_TIMEZONE'] = 'UTC'

# Apply the configuration to the app
Config.init_app(app)

# Instantiate the Babel object
babel = Babel(app)

if __name__ == '__main__':
    app.run()
