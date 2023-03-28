# Return current logged in user from the token generated

import uuid

class CurrentUserModel:
    def __init__(self, id: uuid, name: str, email: str):
        self.id = id
        self.name = name
        self.email = email
