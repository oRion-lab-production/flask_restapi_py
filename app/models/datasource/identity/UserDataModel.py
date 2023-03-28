# user model ORM

import uuid
import sqlalchemy_utils

from app import db
from datetime import datetime


class UserDataModel(db.Model):
    __tablename__ = "identity_user"

    id = db.Column('id', sqlalchemy_utils.UUIDType(binary = False), primary_key = True, default = uuid.uuid4)
    roleId = db.Column('role_id', sqlalchemy_utils.UUIDType(binary = False), nullable = False)
    publicId = db.Column('public_id', db.String(32), nullable = False)
    name = db.Column('name', db.String(255), nullable = False)
    email = db.Column('email', db.String(255), nullable = False)
    password = db.Column('password', db.String(255), nullable = False)
    createdBy = db.Column('created_by', db.String(255))
    createdDT = db.Column('created_datetime', db.DATETIME(6), default = datetime.now)
    modifiedBy = db.Column('modified_by', db.String(255))
    modifiedDT = db.Column('modified_datetime', db.DATETIME(6), default = datetime.now, onupdate = datetime.now)

    # role = db.relationship("RoleDataModel", backref = 'user', lazy = 'dynamic', uselist = False, primaryjoin = "UserDataModel.roleId == RoleDataModel.id")

    def __int__(self, roleId: uuid, publicId: str, name: str, email: str, password: str, createdBy: str = None, createdDT: datetime = None, modifiedBy: str = None, modifiedDT: datetime = None) -> None:
        self.roleId = roleId
        self.name = name
        self.createdBy = createdBy
        self.createdDT = createdDT
        self.modifiedBy = modifiedBy
        self.modifiedDT = modifiedDT

    def __repr__(self):
        return "<User({})>".format(self.model)

    '''def setRole(self, role):
        if role is not None:
            self.roleId = role.id
            self.role = role'''
