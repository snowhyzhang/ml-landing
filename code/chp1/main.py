from weather_forecast import get_city_forecasts

def main():
    forecast_data = get_city_forecasts(['上海', '北京', '广州'])
    print(forecast_data)
    

main()
