from preprocessing import Preprocessor

if __name__ == '__main__':
    preprocessor = Preprocessor()
    
    # 预处理训练集
    print('--------')
    print('训练集')
    train_data = preprocessor.preprocess_data('pfm_data_train.xlsx')
    # 保存变换器
    preprocessor.save_transformer('pfm_preprocessor.pickle')
    print(train_data[:5, :])
    print('--------')
    print('测试集：')
    # 读取变换器
    preprocessor.load_transformer('pfm_preprocessor.pickle')
    # 预处理测试集
    test_data = preprocessor.preprocess_data('pfm_data_test.xlsx', train_or_test=1)
    print(test_data[:5, :])