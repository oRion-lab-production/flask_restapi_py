# role model ORM

import uuid

import sqlalchemy_utils

from app import db
from datetime import datetime


class RoleDataModel(db.Model):
    __tablename__ = "identity_role"

    id = db.Column('id', sqlalchemy_utils.UUIDType(binary = False), primary_key = True, default = uuid.uuid4)
    name = db.Column('name', db.String(10), nullable = False)
    createdBy = db.Column('created_by', db.String(255))
    createdDT = db.Column('created_datetime', db.DATETIME(6), default = datetime.now)
    modifiedBy = db.Column('modified_by', db.String(255))
    modifiedDT = db.Column('modified_datetime', db.DATETIME(6), default = datetime.now, onupdate = datetime.now)

    def __init__(self, name: str, createdBy: str = None, createdDT: datetime = None, modifiedBy: str = None, modifiedDT: datetime = None) -> None:
        self.name = name
        self.createdBy = createdBy
        self.createdDT = createdDT
        self.modifiedBy = modifiedBy
        self.modifiedDT = modifiedDT

    def __repr__(self):
        return "<Role({})>".format(self.model)

