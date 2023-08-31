#! usr/bin/python3
'''
    script that starts a Flask web application
'''

from flask import Flask

"""
Access to the flask and get
from the Flask.
"""

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def super(text):
    return("C {}".format(text.replace("_", " ")))


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def magic(text):
    return ("Python {}".format(text.replace("_", " ")))


@app.route("/number/<int:n>", strict_slashes=False)
def pythonc(n):
    return("{} is a number" .format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def loading_html(n):
    return (render_template('5-number.html', number=n))


if __name__ == "__main__":
    app.run(port="5000")
