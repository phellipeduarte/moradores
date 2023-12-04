from flask import Flask
from flask_restful import Api
from controller.Moradores import Moradores
from controller.Morador import Morador

app = Flask(__name__)
api = Api(app)

api.add_resource(Moradores, "/")
api.add_resource(Morador, "/<int:id>")


if __name__ == "__main__":
    app.run(debug=True)
