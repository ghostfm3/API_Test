import requests
import re


class InfomationWeather:

    def __init__(self,city_code):
        self.url = "https://weather.tsukumijima.net/api/forecast/city/" + city_code
        
    
    def info_temperature(self,day_num):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e: 
            print("Error:{}".format(e))
        
        weather_json = response.json()
        return weather_json['forecasts'][day_num]['chanceOfRain']
    
    def info_datail_weather(self,day_num):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e: 
            print("Error:{}".format(e))
        
        weather_json = response.json()
        weather_datail = weather_json['forecasts'][day_num]['detail']['weather']
        return weather_datail.replace('\u3000', '')
        
