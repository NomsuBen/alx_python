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

if __name__ == "__main__":
    app.run(port="5000")
