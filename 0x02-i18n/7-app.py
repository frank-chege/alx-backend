#!/usr/bin/env python3
'''get the locale'''
from flask import request, render_template, Flask, g
from flask_babel import Babel
import pytz

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
        return users.get(id)
   
    return None

@app.before_request
def before_request():
    user = get_user()
    name = None
    if user:
        g.user = user
        bool = True
        name = g.user['name']
    else:
        g.user = None
        bool = False
    return render_template('0-index.html', bool=bool, name=name)

def get_locale():
    '''gets the locale'''
    locale = request.args.get('locale')
    if locale is not None:
        return locale
    if g.user is not None:
        if g.user['locale'] not in app.config['LANGUAGES']:
            return app.config['BABEL_DEFAULT_LOCALE']
        return g.user['locale']
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_timezone():
    '''returns the user's local time'''
    time_zone = request.args.get('timezone')
    if time_zone:
        try:
            pytz.timezone(time_zone)
        except pytz.UnknownTimeZoneError:
            return None
        return time_zone
    if g.user is not None:
        time_zone = g.user['timezone']
        try:
            pytz.timezone(time_zone)
        except pytz.UnknownTimeZoneError:
            return None
        return time_zone
    return app.config['DEFAULT_TIMEZONE']



babel.init_app(app, locale_selector=get_locale)

@app.route('/', methods=['GET'])
def index():
    '''returns the index page'''
    return render_template('5-index.html')

if __name__ == '__main__':
    app.run(debug=True)