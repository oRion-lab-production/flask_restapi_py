
from flask import Blueprint
from flask_restful import Api
from app.rest.https.admin import indexAPI
from app.rest.https.admin import RegisterAPI
from app.rest.https.admin import LoginAPI
from app.rest.https.admin import RoleAPI


api_admin = Blueprint('api_admin', __name__)
api = Api(api_admin)

# index
api.add_resource(indexAPI, "/")

# register
api.add_resource(RegisterAPI, "/register/")

# login
api.add_resource(LoginAPI, "/login/")

# testing token using role
api.add_resource(RoleAPI, "/role/<string:id>/")
