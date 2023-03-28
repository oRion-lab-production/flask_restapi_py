
from flask import Blueprint
from flask_restful import Api
from app.rest.https.frontend import indexAPI


api_frontend = Blueprint('api_frontend', __name__)
api = Api(api_frontend)

api.add_resource(indexAPI, "/")
