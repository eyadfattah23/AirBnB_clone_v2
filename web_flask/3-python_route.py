#!/usr/bin/python3
'''
script that starts a Flask web application
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ”, followed by the value of the text variable
    /python/<text>: “Python ”,followed by the value of the text variable
'''
from flask import Flask
from markupsafe import escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """display “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """display “HBNB”"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_text(text):
    """display “C ” followed by the value of the text variable """
    return f"C {escape(text.replace('_', ' '))}"


@app.route('/python', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """display “Python ” followed by the value of the text variable """
    return f"Python {escape(text.replace('_', ' '))}"


if __name__ == "__main__":
    app.run(debug=True)
