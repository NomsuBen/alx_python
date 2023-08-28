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
def c_text():
    text = text.replace("_", "")
    return "C " + text

if __name__ == "__main__":
    app.run(port="5000")
