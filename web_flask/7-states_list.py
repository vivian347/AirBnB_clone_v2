#!/usr/bin/python3
"""Falsk application that Returns States
"""
from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exceptions):
    """Perfoms cleanup
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Returns States when route is accessed
    """
    state_obj = storage.all("State")
    return render_template("7-states_list.html",
                           states=[value for value in state_obj.values()])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
