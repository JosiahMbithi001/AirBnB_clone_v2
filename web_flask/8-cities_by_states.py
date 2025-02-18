#!/usr/bin/python3

"""This Script renders  and displays Cities in each State"""

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def city_state():
    """Renders Citiesby State"""
    state = storage.all(State)
    return render_template("8-cities_by_states.html", state=state)


@app.teardown_appcontext
def clean(exception=None):
    """Tearsdown Connection"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
