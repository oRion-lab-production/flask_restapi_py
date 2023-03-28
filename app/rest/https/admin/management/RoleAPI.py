# manage -> role API

import uuid

from flask import jsonify, request
from flask_restful import Resource
from app.repositories import RoleRepository
from app.rest.functions.tokenFunction import token_required


class RoleAPI(Resource):
    _roleRepo = RoleRepository()

    @token_required
    def get(self, currentUser, id: str = None):
        if id is None:
            roles = self._roleRepo.get()
            return jsonify({
                'name': currentUser.name,
                'role': [{
                    'name': role.name
                } for role in roles]
            })
        else:
            role = self._roleRepo.getById(id)
            return jsonify({
                'name': currentUser.name,
                'role': {
                    'name': role.name
                }
            })

