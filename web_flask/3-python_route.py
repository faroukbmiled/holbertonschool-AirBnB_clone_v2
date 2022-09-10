#!/usr/bin/python3
"""task 1"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def flask_hello():
    """prints the bellow return msg!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def flask_hbnb():
    """prints the bellow return msg! under /hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def flask_croute(text):
    """/c/<text>"""
    croute = f'C {text}'.replace('_', ' ')
    return croute


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def flask_py(text="is cool"):
    """display “Python ”, followed by a value..."""
    pyroute = 'Python {}'.format(text).replace("_", " ")
    return pyroute


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
