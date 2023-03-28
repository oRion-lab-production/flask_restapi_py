# role repo

import uuid

from app import db
from datetime import datetime
from ...models.dataobject import CurrentUserModel
from ...models.datasource import RoleDataModel


class RoleRepository:
    def get(self):
        return RoleDataModel.query.all()

    def getById(self, id: uuid) -> RoleDataModel:
        return RoleDataModel.query.get(id)

    def getByName(self, name: str) -> RoleDataModel:
        return RoleDataModel.query.filter_by(name = name).one()

    def create(self, name: str) -> None:
        try:
            role: RoleDataModel = RoleDataModel(
                name = name,
                createdBy = "SYSTEM",
                createdDT = datetime.now()
            )

            db.session.add(role)
            db.session.flush()
            db.session.commit()
        except(ValueError, Exception):
            db.session.rollback()
            raise
        finally:
            db.session.close()

    def update(self, currentUser: CurrentUserModel, id: uuid, name: str) -> None:
        try:
            role: RoleDataModel = self.getById(id)

            if role is None:
                raise Exception("Role not found.")

            role.name = name
            role.modifiedBy = currentUser.name
            role.modifiedDT = datetime.now()

            db.session.add(role)
            db.session.flush()
            db.session.commit()
        except(ValueError, Exception):
            db.session.rollback()
            raise
        finally:
            db.session.close()

    def delete(self, id: uuid) -> None:
        try:
            role: RoleDataModel = self.getById(id)

            if role is None:
                raise Exception("Role not found.")

            db.session.delete(role)
            db.session.flush()
            db.session.commit()
        except(ValueError, Exception):
            db.session.rollback()
            raise
        finally:
            db.session.close()
