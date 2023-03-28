# return services application

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker

from .config import Config

application = Flask(__name__)  # Creating application

cors = CORS(
    application,
    resources = {r"/api/*": {"origins": "*"}},
    methods = ["GET, HEAD, OPTIONS, POST, PUT"],
    allow_headers = "Access-Control-Allow-Origin",
    supports_credentials = True,
)

application.config.from_object(Config)

engine = create_engine(application.config['SQLALCHEMY_DATABASE_URI'])
db = SQLAlchemy(application)

migrate = Migrate(application, db)

from app.models.datasource import *

db.init_app(application)
Session = sessionmaker()
Session.configure(bind=engine)

# Initialise the database session
session = Session()
session._model_changes = {}





