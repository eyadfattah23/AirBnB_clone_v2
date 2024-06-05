#!/usr/bin/python3
'''
script that starts a Flask web application
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed the text variable
                (replace underscore _ symbols with a space )
    /python/<text>: “Python ”,followed by the value of the text variable
'''
from flask import Flask

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # , debug=True)
