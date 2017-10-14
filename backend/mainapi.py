from flask import Flask
from flask_restful import Resource, Api
from backend.core import Core


app = Flask(__name__)
api = Api(app)
core = Core()


class LikeDestination(Resource):
    def get(self):
        return core.like_destination().to_json()

api.add_resource(LikeDestination, '/like_destination')

if __name__ == '__main__':
    app.run(debug=True)