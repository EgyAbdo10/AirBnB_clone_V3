#!/usr/bin/python3
"""retrieve state objects"""
from models.state import State
from flask import jsonify
from flask_restful import Resource, abort, request
from models import storage


def abortNotExists(cls, obj_id):
    """exit with a 404 status if obj not found"""
    obj = storage.get(cls, obj_id)
    if obj is None:
        abort(404)
    return obj


class State_view_all(Resource):
    """handle all states requests without id"""
    def get(self):
        """get all state objects"""
        objs_dict = storage.all()
        obj_list = []
        for obj in objs_dict.values():
            obj_list.append(obj.to_dict())
        return jsonify(obj_list)

    def post(self):
        """Creates a State: POST /api/v1/states"""
        try:
            data = request.get_json()
        except Exception:
            abort(400, message="Not a JSON")
        if "name" not in data.keys():
            abort(400, message="Missing name")

        new_obj = State(**data)
        storage.new(new_obj)
        return new_obj.to_dict(), 201


class State_view(Resource):
    """handle all states requests with id"""
    def get(self, state_id):
        """Retrieves a State object: GET /api/v1/states/<state_id>"""
        obj = abortNotExists(State, state_id)
        return jsonify(obj.to_dict())

    def delete(self, state_id):
        """Deletes a State object:: DELETE /api/v1/states/<state_id>"""
        obj = abortNotExists(State, state_id)
        storage.delete(obj)
        return {}, 200

    def put(self, state_id):
        """Updates a State object: PUT /api/v1/states/<state_id>"""
        obj = abortNotExists(State, state_id)
        try:
            data = request.get_json()
        except Exception:
            abort(400, message="Not a JSON")

        for key, val in data.items():
            if key not in ["id", "created_at", "updated_at"]:
                setattr(obj, key, val)

        storage.new(obj)
        return obj.to_dict(), 200
