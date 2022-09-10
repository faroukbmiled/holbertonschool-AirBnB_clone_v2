#!/usr/bin/env python3
"""task 1"""
from tokenize import Number
from flask import Flask, render_template
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
    pyroute = f'Python {text}'.replace("_", " ")
    return pyroute


@app.route('/number/<int:n>', strict_slashes=False)
def flask_number(n):
    """number route"""
    numroute = '{} is a number'.format(n)
    return numroute


@app.route('/number_template/<int:n>', strict_slashes=False)
def flask_html(n):
    """display html if number"""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
