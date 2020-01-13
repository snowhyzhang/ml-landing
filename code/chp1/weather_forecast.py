import json
import re

import pandas as pd
import requests

# 配置API地址
URL = 'http://wthrcdn.etouch.cn/weather_mini'
# 配置处理风力的正则表达式
FENGLI_REX = re.compile('[0-9]*[<-][0-9]*级')


def get_city_forecast(city):
    """
    获取城市的天气预报
    :param city: 城市
    :return: 天气预报
    """
    response = requests.get(URL, params={'city': city})
    content = json.loads(response.content)
    df = pd.DataFrame(content['data']['forecast'])
    # 对形如<![CDATA[3-4级]]>风力数据进行处理，保留其中的级数
    df['fengli'] = df['fengli'].map(lambda x: FENGLI_REX.findall(x)[0])
    # 处理高温和低温的字样
    df['high'] = df['high'].map(lambda x: x.replace('高温 ', ''))
    df['low'] = df['low'].map(lambda x: x.replace('低温 ', ''))
    df['city'] = city
    
    return df


def get_city_forecasts(city_list):
    """
    获取列表中城市的天气预报
    :param city: 城市列表
    :return: 天气预报
    """
    df_list = []
    for city in city_list:
        df = get_city_forecast(city)
        df_list.append(df)
        
    return pd.concat(df_list)
