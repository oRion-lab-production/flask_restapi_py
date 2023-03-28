# sign up services

import uuid

from ...repositories import RoleRepository
from ...repositories import UserRepository
from werkzeug.security import generate_password_hash


class SignUpService:
    _roleRepo = RoleRepository()
    _userRepo = UserRepository()

    def execute(self, request):
        try:
            hashed_password = generate_password_hash(request['password'], method = 'sha256')

            role = self._roleRepo.getByName(request['role'])
            if role is None:
                return 'Role not found.'

            self._userRepo.create(role, str(uuid.uuid4().hex), request['name'], request['email'], hashed_password)
            return 'User created successfully'
        except Exception as ex:
            return str(ex)


