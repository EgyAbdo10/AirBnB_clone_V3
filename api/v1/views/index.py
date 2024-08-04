#!/usr/bin/python3
"""routes of the app_view blueprint"""
# from api.v1.views import app_views avoid circular import
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


def register_routes(app_views):
    """register all routes of blueprint app_views"""
    @app_views.route("/status")
    def get_status():
        """return status OK"""
        return jsonify({"status": "OK"})

    @app_views.route("/stats")
    def get_stats():
        """get objects count"""
        stats = {}
        for cls_name, cls in classes.items():
            stats[cls_name] = storage.count(cls)

        return jsonify(stats)
