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


if __name__ == '__main__':
    app.run(app.run(host="0.0.0.0", port="5000"))
