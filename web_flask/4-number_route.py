#!/usr/bin/python3
"""This Script Returns A Confirmation that input n is a Number """


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

    return 'C ' + text.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text=None):
    """
    A Python Method that displays Python is Cool by Default
    else returns Python +  passed in text
    """
    if text:
        return "Python " + text.replace('_', ' ')
    else:
        return "Python is cool"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """A Method that returns n if n is an int"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
