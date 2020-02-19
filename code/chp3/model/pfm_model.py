import pickle

from imblearn.over_sampling import SMOTE
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV


class Modeler:
    def __init__(self, x, y):
        """

        :param x: 特征
        :param y: 标签
        """
        self.x = x
        self.y = y

        # 最佳超参数
        self.best_hyper_params = None
        # 模型
        self.model = None

    def smote(self):
        """
        使用SMOTE算法来平衡数据
        :return:
        """
        print('using smote.')
        sm = SMOTE()
        self.x, self.y = sm.fit_resample(self.x, self.y)        
        
    def determine_hyper_params(self):
        """
        确定最佳的超参数
        :return:
        """
        lr = LogisticRegression()
        # 设定候选超参数
        params = [{'C': [2 ** i for i in range(-10, 10)]}]

        # 通过交叉验证的方式搜索最佳参数
        gs_lr = GridSearchCV(
            estimator=lr,
            param_grid=params,
            # 设定10折交叉验证
            cv=10,
            # 选择auc作为，模型评估指标
            scoring='roc_auc')
        gs_lr.fit(self.x, self.y)
        print('best hyper params: {}'.format(gs_lr.best_params_))
        self.best_hyper_params = gs_lr.best_params_

    def train_model(self):
        """
        训练模型
        :return:
        """
        if self.best_hyper_params is None:
            # 如果没有交叉验证选取最佳的参数，则默认设置为1.0
            self.best_hyper_params = {'C': 1.0}
            print('using hyper params: {}'.format(self.best_hyper_params))

        self.model = LogisticRegression(C=self.best_hyper_params['C'])
        self.model.fit(self.x, self.y)
        print('training model is done.')

    def save_model(self, file_path):
        """
        保存模型
        :param file_path: 模型保存路径
        :return:
        """
        if self.model is None:
            print('model is not trained!')
            return

        with open(file_path, 'wb') as f:
            print('saving model to file: {}'.format(file_path))
            pickle.dump(self.model, f)

