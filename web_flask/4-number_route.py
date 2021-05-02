#!/usr/bin/python3
"""
Script to start a Flask web application
"""
from flask import Flask
app = Flask(__name__)
host = '0.0.0.0'
port = '5000'


@app.route('/', strict_slashes=False)
def hello_route():
    """
    Return Hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello():
    """
    Return HBNB
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """
    Return C is <>
    """
    rm_text_dash = text.replace('_', ' ')
    return 'C {}'.format(rm_text_dash)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_python(text='is cool'):
    """
    Return python is cool unless user changes entry
    """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def check_int(n):
    """
    Check if a number is an integer
    """
    if isinstance(n, int) is True:
        return '{} is a number'.format(n)

if __name__ == '__main__':
    app.run(host, port)
