import os
from flask import Flask, render_template

app = Flask(__name__)

THEME_FILE = os.path.join(os.path.dirname(__file__), 'theme_settings.py')


def theme_settings():
    variables = {}
    with open(THEME_FILE) as f:
        exec(f.read(), variables, variables)
    return variables


@app.route('/')
def home():
    return render_template('strapped.html', **theme_settings())
