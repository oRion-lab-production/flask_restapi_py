# manage -> register API

from flask import jsonify, request
from flask_restful import Resource
from app.services import SignUpService


class RegisterAPI(Resource):
    _signUpSvc = SignUpService()

    def post(self):
        return jsonify({
            'message': self._signUpSvc.execute(request.get_json())
        })
