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
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    '''display a HTML page in  9-states.html'''
    from models.state import State

    states = storage.all(State)
    stated = None
    if id:
        for state in states.values():
            if id == state.id:
                stated = state
                break

    return render_template('9-states.html', states=states, stated=stated)


@app.teardown_appcontext
def teardown_appcontext(exc):
    ''' remove the current SQLAlchemy Session '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # , debug=True)
