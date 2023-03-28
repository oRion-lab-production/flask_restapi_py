# login services

import jwt

from app import application
from flask import make_response
from datetime import datetime, timedelta
from ...repositories import UserRepository
from werkzeug.security import check_password_hash


class LoginService:
    _userRepo = UserRepository()

    def exceute(self, request):
        try:
            auth = request.authorization

            if not auth or not auth.username or not auth.password:
                return make_response('could not verify', 401, {'Authentication': 'login required"'})

            user = self._userRepo.getByName(auth.username)
            if user is None:
                return make_response('User did not exist', 400, {'Authentication': 'Please register this user."'})

            if check_password_hash(user.password, auth.password):
                token = jwt.encode(
                    {'public_id': user.publicId, 'exp': datetime.utcnow() + timedelta(minutes = 45)},
                    application.config['SECRET_KEY'],
                    "HS256"
                )
                return token

            return make_response('could not verify', 401, {'Authentication': '"login required"'})
        except Exception as ex:
            return str(ex)

