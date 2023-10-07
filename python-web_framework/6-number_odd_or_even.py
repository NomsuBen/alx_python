#! usr\bin\python3

'''
  Write a script that starts a Flask web application:
'''

from flask import Flask, render_template

'''
  Flask imported
'''

app = Flask(__name__)


@app.route("/")
def home():
  return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
  return "HBNB"


@app.route("/c/<text>")
def c(text):
  return("C {}".format(text.replace("_", " ")))

@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<text>")
def python(text):
  return("Python {}".format(text.replace("_", " ")))


@app.route("/number/<int:n>")
def number(n):
  return("{} is a number" .format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def template(n):
  return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_even(n):
    return (render_template('6-number_odd_or_even.html', number=n))
  


if __name__=="__main__":
  app.run(debug=True, port="5000")