import pickle

from preprocess.preprocessor import Preprocessor


class Predictor:
    def __init__(self, preprocessor_path, model_path):
        """

        :param preprocessor_path: 预处理器路径
        :param model_path: 模型路径
        """
        self.preprocessor_path = preprocessor_path
        self.model_path = model_path

        self.preprocessor = None
        self.model = None

    def load_model(self):
        """
        读取模型和预处理器
        :return:
        """
        # 读取预处理器
        self.preprocessor = Preprocessor()
        self.preprocessor.load_transformer(self.preprocessor_path)

        # 读取模型
        with open(self.model_path, 'rb') as f:
            print('loading model from {}'.format(self.model_path))
            self.model = pickle.load(f)

    def predict(self, data):
        """
        进行预测
        :param data: 数据
        :return:
        """
        if self.preprocessor is None or self.model is None:
            print('preprocessor or model is None!')
            return -1

        data = self.preprocessor.preprocess_data(data, train_or_test=1)
        result = self.model.predict(data)
        return result.tolist()
