# frontend -> index API

from flask_restful import Resource
from flask_restful.reqparse import RequestParser


class indexAPI(Resource):
    def __init__(self):
        self.parser = RequestParser()

    def get(self):
        return "HI this is front end"

