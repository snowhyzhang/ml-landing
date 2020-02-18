import pickle

import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, KBinsDiscretizer


class Preprocessor:
    def __init__(self):
        # 待转为str类型的列
        self.to_str_cols = ['Education', 'JobSatisfaction']
        # id列
        self.id_col = 'EmployeeNumber'
        # 待去掉的列
        self.to_rm_cols = ['StandardHours', 'Over18']
        # 变换器
        self.column_transformer = None

    def load_data(self, file_path):
        """
        读取数据
        :param file_path: 文件路径
        :return:
        """
        # 读取数据集
        data = pd.read_excel(file_path)
        # 将有缺失值的样本去除
        data = data.dropna()
        print('data shape@{}'.format(data.shape))
        # 将转为str类型
        data[self.to_str_cols] = data[self.to_str_cols].astype(str)
        return data

    def remove_columns(self, data):
        """
        去掉可以删除的列
        :param data: 数据
        :return:
        """
        # 删除ID列
        data = data.drop(columns=self.id_col)
        # 删除StandardHours和Over18这两列
        data = data.drop(columns=self.to_rm_cols)

        return data

    def transform_train(self, train_data):
        """
        变换训练集
        :param train_data: 训练集
        :return:
        """
        # 数值类型的特征
        num_cols = train_data.select_dtypes(include=np.number).columns.tolist()
        # 去掉年龄特征
        num_cols.remove('Age')
        # 类别类型的特征
        cat_cols = train_data.select_dtypes(include=np.object).columns.tolist()

        self.column_transformer = ColumnTransformer(
            [
                # 对类别型数据做One-Hot编码
                ('one-hot', OneHotEncoder(handle_unknown='ignore'), cat_cols),
                # 对除了数值类型做标准化
                ('scale', StandardScaler(), num_cols),
                # 对age字段做离散化，转化为5个类别
                ('discretizer', KBinsDiscretizer(n_bins=5), ['Age'])
            ]
        )

        return self.column_transformer.fit_transform(train_data)

    def transform_test(self, test_data):
        """
        变换测试集
        :param test_data: 测试集
        :return:
        """
        if self.column_transformer is None:
            print('column transformer is None!')
            return

        return self.column_transformer.transform(test_data)

    def save_transformer(self, file_path):
        """
        保存变换器
        :param file_path: 变换器路径
        :return:
        """
        if self.column_transformer is None:
            print('column transformer is None!')
            return

        with open(file_path, 'wb') as f:
            pickle.dump(self.column_transformer, f)

    def load_transformer(self, file_path):
        """
        读取变换器
        :param file_path: 变换器路径
        :return:
        """
        with open(file_path, 'rb') as f:
            self.column_transformer = pickle.load(f)

    def preprocess_data(self, file_path, train_or_test=0):
        """
        预处理数据集
        :param file_path: 文件路径
        :param train_or_test: 训练或者测试：0 - 训练，1 - 测试
        :return:
        """
        data = self.load_data(file_path)
        data = self.remove_columns(data)
        if train_or_test == 0:
            return self.transform_train(data)
        return self.transform_test(data)
