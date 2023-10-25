#!/usr/bin/python3

"""
Start flask
"""

from flask import Flask, render_template


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
    """function to execute"""
    return "C " + text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
def display_python_text(text):
    """Display 'python' followed by the value of the text variable."""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """ Display 'n is a number' only if n is an integer. """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number(n):
    """
    Template renderer
    """
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_odd_or_even(n):
    """
    display page if int
    """
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html',
                               num=n, text='even')
    return render_template('6-number_odd_or_even.html',
                           num=n, text='odd')


if __name__ == '__main__':
    app.run(app.run(host="0.0.0.0", port="5000"))
