#!/usr/bin/python3

"""
Start flask
"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states(state_id=None):
    """
    displays states
    """
    states = storage.all("State")

    if state_id is not None:
        state_id = 'State.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def shut_db(err):
    """
    shut db
    """
    storage.close()


if __name__ == '__main__':
    app.run(app.run(host="0.0.0.0", port="5000"))
