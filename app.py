from flask import Flask
from flask_restful import Resource, Api
from flask_cors import cross_origin

app = Flask(__name__)
api = Api(app)

parameters = {
    'maxCreditTerm': 80,
    'minCreditTerm': 12,
    'minCreditSum': 1000,
    'maxCreditSum': 1500000,
}

class Parameters(Resource):
    @cross_origin()
    def get(self):
        return parameters

api.add_resource(Parameters, '/')

if __name__ == '__main__':
    app.run()
