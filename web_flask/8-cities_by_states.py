#!/usr/bin/python3
"""Returns Cities when route is accessed
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exceptions):
    """Perfoms Clean up
    """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Returns Cities when route is accessed
    """
    state_obj = storage.all("State")
    city_obj = storage.all("City")
    return render_template("8-cities_by_states.html",
                           states=[value for value in state_obj.values()],
                           cities=[value for value in city_obj.values()])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
