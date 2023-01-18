#!/usr/bin/python3
"""Returns States and Cities when route is accessed
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exceptions):
    """Perfoms Clean up
    """
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def show_states(id=None):
    """Returns States and Cities when route is accessed
    """
    state_obj = storage.all("State")
    city_obj = storage.all("City")

    state_id = "State.{}".format(id)
    if id is not None and state_id not in state_obj:
        states = None
    return render_template("9-states.html",
                           states=[value for value in state_obj.values()],
                           cities=[value for value in city_obj.values()],
                           id=id)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
