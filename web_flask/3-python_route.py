#!/usr/bin/python3

"""
Start flask
"""

from flask import Flask


app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """
    return Hello HBNB!
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def string(text):
    """
    function to execute
    """
    return "C " + text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
def display_python_text(text):
    """
    Display 'python' followed by the value of the text
    """
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(app.run(host="0.0.0.0", port="5000"))
