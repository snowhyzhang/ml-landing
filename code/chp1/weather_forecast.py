import json

import pandas as pd
import requests

URL = 'http://wthrcdn.etouch.cn/weather_mini'


def get_city_forecast(city):
    """
    获取城市的天气预报
    :param city: 城市
    :return: 天气预报
    """
    response = requests.get(URL, params={'city': city})
    content = json.loads(response.content)
    df = pd.DataFrame(content['data']['forecast'])
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
