#!/usr/bin/python3
"""
- script that starts a Flask web application

- web application listening on 0.0.0.0, port 5000

- use storage for fetching data from the storage engine

- After each request you must remove the current SQLAlchemy Session:
    Declare a method to handle @app.teardown_appcontext
    Call in this method storage.close()

- Routes:
    /states_list: display a HTML page
"""
from models import storage
from models.state import State
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """display “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route('/states_list', strict_slashes=False)
def list_states():
    """display a HTML page

    Returns:
        html file: the list of all State objects present in DBStorage
    """
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_appcontext(ctx):
    """After each request remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
