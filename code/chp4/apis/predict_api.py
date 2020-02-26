from flask_restful import Resource, reqparse
import pandas as pd

from backend.predictor import Predictor

args = reqparse.RequestParser()
args.add_argument('data', type=dict, action='append', required=True)


predictor = Predictor('preprocessor.pickle', 'logistics.model')
predictor.load_model()


class Predict(Resource):
    def post(self):
        data = args.parse_args()
        data = pd.DataFrame(data['data'])

        result = predictor.predict(data)
        return result


class Reload(Resource):
    def get(self):
        predictor.load_model()

        return 'message: success to reload model'
