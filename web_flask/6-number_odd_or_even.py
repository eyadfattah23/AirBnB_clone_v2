#!/usr/bin/python3
'''
script that starts a Flask web application
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
	/c/<text>: display “C ”, followed by the value of the text variable
	/python/(<text>): display “Python ”, followed by the value of the text variable 
	/number/<n>: display “n is a number” only if n is an integer
	/number_template/<n>: display a HTML page only if n is an integer
	/number_odd_or_even/<n>: display a HTML page only if n is an integer: 
'''
from flask import Flask, render_template
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
def python_text(text='is_cool'):
    """display “Python ” followed by the value of the text variable """
    return f"Python {escape(text.replace('_', ' '))}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """display “n is a number” only if n is an integer"""
    return f"{escape(n)} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """display a HTML page only if n is an integer"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(debug=True)
