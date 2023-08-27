'''
    script that starts a Flask web application
'''

import flask from Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello HBNB!"

if __name__ == 0-hello_route:
    app.run(strict_slashes=False, port="5000")