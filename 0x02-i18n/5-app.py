#!/usr/bin/env python3
'''get the locale'''
from flask import request, render_template, Flask, g
from flask_babel import Babel

class Config:
    '''configure the app'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    '''returns the user passed in the url'''
    id = request.args.get('login_as')
    if id is not None:
        id = int(id)
    if id in users:
        return users.get(id)['name']
   
    return None

@app.before_request
def before_request():
    user = get_user()
    if user:
        g.user = user
        bool = True
    else:
        g.user = None
        bool = False
    return render_template('0-index.html', bool=bool, name=g.user)

def get_locale():
    '''gets the locale'''
    locale = request.args.get('locale')
    if locale == 'fr':
        return 'fr'
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])

babel.init_app(app, locale_selector=get_locale)

@app.route('/', methods=['GET'])
def index():
    '''returns the index page'''
    return render_template('5-index.html')

if __name__ == '__main__':
    app.run(debug=True)