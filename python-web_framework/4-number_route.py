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


@app.route("/c/julien")
def julien():
    return "C julien"


@app.route("/c/is_super_fun")
def super():
    return "C is super fun"


@app.route("/python/test")
def magic():
    return "Python test"


@app.route("/python/this_is_a_test")
def python():
    return "Python this is a test"


@app.route("/python/")
def pythonc():
    return "Python is cool"


@app.route("/number/333")


def numberc():
    return "333 is a number"

if __name__ == "__main__":
    app.run(port="5000")
