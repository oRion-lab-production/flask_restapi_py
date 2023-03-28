# user repo

import uuid

from app import db
from datetime import datetime
from ...models.dataobject import CurrentUserModel
from ...models.datasource import RoleDataModel
from ...models.datasource import UserDataModel


class UserRepository:
    def get(self):
        return UserDataModel.query.all()

    def getById(self, id: uuid) -> UserDataModel:
        return UserDataModel.query.get(id)

    def getByName(self, name: str) -> UserDataModel:
        return UserDataModel.query.filter_by(name = name).one()

    def getByEmail(self, email: str) -> UserDataModel:
        return UserDataModel.query.filter_by(email = email).one()

    def create(self, role: RoleDataModel, publicId: str, name: str, email: str, password: str) -> None:
        try:
            user = UserDataModel(
                roleId = role.id,
                publicId = publicId,
                name = name,
                email = email,
                password = password,
                createdBy = "SYSTEM",
                createdDT = datetime.now()
            )

            db.session.add(user)
            db.session.flush()
            db.session.commit()
        except(ValueError, Exception):
            db.session.rollback()
            raise
        finally:
            db.session.close()

    def update(self, currentUser: CurrentUserModel, id: uuid, password: str) -> None:
        try:
            user: UserDataModel = self.getById(id)

            if user is None:
                raise Exception("User not found.")

            user.password = password
            user.modifiedBy = currentUser.name
            user.modifiedDT = datetime.now()

            db.session.add(user)
            db.session.flush()
            db.session.commit()
        except(ValueError, Exception):
            db.session.rollback()
            raise
        finally:
            db.session.close()

    def delete(self, id: uuid) -> None:
        try:
            user: UserDataModel = self.getById(id)

            if user is None:
                raise Exception("User not found.")

            db.session.delete(user)
            db.session.flush()
            db.session.commit()
        except(ValueError, Exception):
            db.session.rollback()
            raise
        finally:
            db.session.close()
