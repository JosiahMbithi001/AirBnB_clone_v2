#!/usr/bin/python3

"""This Script renders  and displays states"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """Renders State Template"""
    state = storage.all(State)
    return render_template("7-states_list.html", state=state)


@app.teardown_appcontext
def clean(exception=None):
    """Tearsdown Connection"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
