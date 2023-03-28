# token model object

import json

import jwt

from app import application
from flask import jsonify, request
from functools import wraps
from ...models.dataobject import CurrentUserModel
from ...models.datasource import UserDataModel


def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})

        try:
            data = jwt.decode(token, application.config['SECRET_KEY'], algorithms = ["HS256"])
            user: UserDataModel = UserDataModel.query.filter_by(publicId = data['public_id']).one()
            kwargs['currentUser'] = CurrentUserModel(user.id, user.name, user.email)
        except:
            return jsonify({'message': 'a valid token is required'})

        return f(*args, **kwargs)
    return decorator
