# config get env secret

import os
from dotenv import load_dotenv

load_dotenv()


class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', '33de7c0967ec38bacd3d6481b9ad8d2c')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL',
                                             'mysql://root:root@localhost/testingschema')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # This is just here to suppress a warning from SQLAlchemy as it will soon be removed
