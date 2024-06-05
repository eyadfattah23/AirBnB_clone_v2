#!/usr/bin/python3
'''
script that starts a Flask web application
Routes:
    /: display “Hello HBNB!”

    /hbnb: display “HBNB”

    /c/<text>: display “C ” followed the text variable
                (replace underscore _ symbols with a space )

    /python/<text>: “Python ”,followed by the value of the text variable

    /number/<n>: display “n is a number” only if n is an integer

    /number_template/<n>: display a HTML page only if n is an integer:
                H1 tag: “Number: n” inside the tag BODY

    /number_odd_or_even/<n>: display a HTML page only if n is an integer:
                H1 tag: “Number: n is even|odd” inside the tag BODY


'''
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """display “Hello HBNB!”

    Returns:
        str:  “Hello HBNB!”
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """display HBNB”

    Returns:
        str:  "HBNB”
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def C_text(text):
    """display display “C ” followed by value of text variable

    Returns:
        str:  "C <text>"
    """

    return f"C {text.replace('_', ' ')}"
    # return f"C {escape(text.replace('_', ' '))}"


@app.route("/python", strict_slashes=False)
# @app.route('/python', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text='is cool'):
    """display display “python ” followed by value of text variable

    Returns:
        str:  "Python <text>/is cool"
    """

    return f"Python {text.replace('_', ' ')}"
    # return f"Python {escape(text.replace('_', ' '))}"


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """display “n is a number” only if n is an integer"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer

    H1 tag: “Number: n” inside the tag BODY
"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """display a HTML page only if n is an integer

    H1 tag: “Number: n is even|odd” inside the tag BODY

"""
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # , debug=True)
