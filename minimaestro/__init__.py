import os
from flask import Flask, render_template

app = Flask(__name__)

THEME_FILE = os.path.join(os.path.dirname(__file__), 'theme_settings.py')


_themedata = None

def theme_settings():
    global _themedata
    if _themedata is None or app.debug:
        _themedata = {}
        with open(THEME_FILE) as f:
            exec(f.read(), _themedata, _themedata)
    return _themedata


@app.route('/')
def home():
    return render_template('strapped.html', **theme_settings())
