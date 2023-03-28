# manage -> login API

from flask import jsonify, request
from flask_restful import Resource
from app.services import LoginService


class LoginAPI(Resource):
    _loginSvc = LoginService()

    def post(self):
        token = self._loginSvc.exceute(request)

        return jsonify({
            'token': token
        })
