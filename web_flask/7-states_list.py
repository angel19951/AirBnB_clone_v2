#!/usr/bin/python3
"""
Script to start a Flask web application
"""
from flask import Flask
from flask import render_template
from models import storage
from models.states import State

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


@app.route('/number_template/<int:n>', strict_slashes=False)
def check_html_int(n):
    """
    Display html file content if number is an integer
    """
    if isinstance(n, int) is True:
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def html_even_odd(n):
    """
    Display html file content telling if number is odd or even
    """
    if isinstance(n, int) is True:
        return render_template('6-number_odd_or_even.html', n=n)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """
    List all states from a database
    """

    states = storage.all(State)
    states_list = []

    for key, val in states.items():
        states_list.append(val)

    return render_template('7-states_list.html', states_list=states_list)


@app.teardown_appcontext
def tear_down(self):
    """
    Teardown of the app c
    """
    storage.close()


if __name__ == '__main__':
    app.run(host, port)