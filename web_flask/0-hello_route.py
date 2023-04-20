#!/usr/bin/python3
"""This Script Starts A Flask Web App & returns "Hello HBNB" """


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """A Method to return Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
