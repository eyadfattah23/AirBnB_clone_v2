#!/usr/bin/python3
"""
- script that starts a Flask web application

- web application listening on 0.0.0.0, port 5000

- use storage for fetching data from the storage engine

- After each request you must remove the current SQLAlchemy Session:
    Declare a method to handle @app.teardown_appcontext
    Call in this method storage.close()

- Routes:
    /states: display a HTML page
    /states/<id>: display a HTML page
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


@app.teardown_appcontext
def teardown_appcontext(exception):
    """After each request remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def list_states(id=None):
    """display a HTML page

    Returns:
        html file: the list of all State objects present in DBStorage
    """
    states = storage.all(State)
    stated = None
    if id:
        for state in states.values():
            if state.id == id:
                stated = state
                break

    return render_template('9-states.html', states=states,
                           stated=stated, id=id)


@app.route('/cities_by_states', strict_slashes=False)
def list_cities_by_state():
    """display a HTML page

    Returns:
        html file: the list of all State objects present in DBStorage
                        with the list of City objects linked to the State
    """
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # , debug=True)