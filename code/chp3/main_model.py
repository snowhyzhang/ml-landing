import pandas as pd

from model.pfm_model import Modeler
from preprocess.preprocessor import Preprocessor

data = pd.read_excel('pfm_data.xlsx')

x = data.drop(columns='Attrition')
y = data['Attrition']

preprocessor = Preprocessor()
x = preprocessor.preprocess_data(data=x)
preprocessor.save_transformer('preprocessor.pickle')

modeler = Modeler(x, y)
modeler.smote()
modeler.determine_hyper_params()
modeler.train_model()
modeler.save_model('logistics.model')
