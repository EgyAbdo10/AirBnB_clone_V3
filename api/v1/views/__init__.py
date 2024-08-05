#!/usr/bin/python3
"""initialize a blueprint"""
from flask import Blueprint
from flask_restful import Api
from api.v1.views.states import *

app_views = Blueprint("app_views", __name__, url_prefix='/api/v1')

from api.v1.views.index import *

api = Api(app_views)

api.add_resource(State_view_all, "/states/")
api.add_resource(State_view, "/states/<state_id>")
