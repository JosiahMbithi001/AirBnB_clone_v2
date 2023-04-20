#!/usr/bin/python3
"""This Script Starts A Flask Web App & returns "Hello HBNB" & "HBNB" """


from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
	"""A Method to return Hello HBNB!"""
	
	return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
	"""A method to return HBNB!"""
	
	return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c(text):
	"""A Method that returns C and text"""

	return f'C {text.replace("_"," ")}'


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)
