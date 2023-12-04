from flask import request
from flask_restful import Resource
from fake_db import fake_db


class Morador(Resource):
    def get(self, id):
        return fake_db[id]

    def put(self, id):
        data = request.get_json()

        fake_db[id]["name"] = data.get("name")

        return fake_db

    def delete(self, id):
        del fake_db[id]
        return fake_db
