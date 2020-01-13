import sqlite3

import pandas as pd


class SQLiteProcessor:
    def __init__(self, file_path):
        """

        :param file_path: SQLite文件路径
        """
        self.file_path = file_path

    def __get_connect(self):
        """
        获取SQLite数据库的链接
        :return:
        """
        return sqlite3.connect(self.file_path)

    def load_data(self, sql, parse_dates=None):
        """
        读取数据
        :param sql: sql语句
        :param parse_dates: 需要转为日期类型的列
        :return:
        """
        conn = None
        # 使用try-catch结构，当发生错误时，保证数据库链接能被正确关闭
        try:
            conn = self.__get_connect()
            return pd.read_sql(conn, sql, parse_dates=parse_dates)
        except sqlite3.Error as e:
            print('SQLite error@{}'.format(e))
        except Exception as e:
            print('Unknown error@{}'.format(e))
        finally:
            conn.close()

    def write_data(self, table_name, df, if_exists='append', is_index=False):
        """

        :param table_name: 数据要插入到的表名称
        :param df: DataFrame
        :param if_exists: to_sql中的if_exists参数，这里我们默认为append
        :param is_index: to_sql中的index参数，这里我们默认为False
        :return:
        """
        conn = None
        try:
            conn = self.__get_connect()
            df.to_sql(table_name, df, if_exists=if_exists, index=is_index)
        except sqlite3.Error as e:
            print('SQLite error@{}'.format(e))
        except Exception as e:
            print('Unknown error@{}'.format(e))
        finally:
            conn.close()


user_sqlite = SQLiteProcessor('data/user.db')
car_sqlite = SQLiteProcessor('data/car.db')
