#!/usr/bin/python3
"""Returns States Cities and Amenities when route is accessed
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exceptions):
    """Perfoms Clean up
    """
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def display_filters():
    """Returns States Cities and Amenities when route is accessed
    """
    state_obj = storage.all("State")
    city_obj = storage.all("City")
    amts_obj = storage.all("Amenity")

    return render_template("10-hbnb_filters.html",
                           states=[value for value in state_obj.values()],
                           cities=[value for value in city_obj.values()],
                           amenities=[value for value in amts_obj.values()])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
