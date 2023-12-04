from flask import request
from flask_restful import Resource
from fake_db import fake_db


class Moradores(Resource):
    def get(self):
        return fake_db

    def post(self):
        item_id = len(fake_db) + 1

        data = request.get_json()

        fake_db[item_id] = {"name": data.get("name")}

        return fake_db
