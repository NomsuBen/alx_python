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
def home():
    return "Hello HBNB!"

if __name__ == "__0-hello_route__":
    app.run(strict_slashes=False, port="5000")