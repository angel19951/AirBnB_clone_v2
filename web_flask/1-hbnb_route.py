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

if __name__ == '__main__':
    app.run(host, port)
