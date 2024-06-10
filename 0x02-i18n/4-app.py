#!/usr/bin/env python3
'''get the locale'''
from flask import request, render_template, Flask
from flask_babel import Babel

class Config:
    '''configure the app'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

def get_locale():
    '''gets the locale'''
    locale = request.args.get('locale')
    if locale == 'fr':
        return 'fr'
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel.init_app(app, locale_selector=get_locale)

@app.route('/', methods=['GET'])
def index():
    '''returns the index page'''
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(debug=True)