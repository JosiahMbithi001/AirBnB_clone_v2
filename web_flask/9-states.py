#!/usr/bin/python3

"""
This Script renders  and displays States and
Cities in a States if a State id is passed
""" 

from models import storage
from models.state import State
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def city_state():
    """Renders Citiesby State"""
    state = storage.all(State)
    return render_template("7-states_list.html", state=state)

@app.route('/states/<id>', strict_slashes=False)
def state_by_id():
	"""Renders an HTML Page if a State.if is found"""
	for state in storage.all(State).values():
		if state.id == id:
			return render_template('9-states.html', state=state, mode='id')
		return render_template('9-states.html', state=state, mode='none')

@app.teardown_appcontext
def clean(exception=None):
    """Tearsdown Connection"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
