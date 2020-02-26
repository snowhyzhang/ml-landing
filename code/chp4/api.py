from flask import Flask
from flask_restful import Api

from apis.predict_api import Predict, Reload

app = Flask(__name__)
api = Api(app)

api.add_resource(Predict, '/predict')
api.add_resource(Reload, '/reload')

if __name__ == '__main__':
    app.run()
