#!/usr/bin/python3
"""Returns States Cities Places and Amenities
    when route is accessed
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exceptions):
    """Perfoms Clean up
    """
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def display_filters():
    """Returns States Cities Places and Amenities
        when route is accessed
    """
    states = storage.all("State")
    cities = storage.all("City")
    amenities = storage.all("Amenity")
    places = storage.all("Place")

    return render_template("100-hbnb.html",
                           states=states,
                           cities=cities,
                           amenities=amenities,
                           places=places)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
