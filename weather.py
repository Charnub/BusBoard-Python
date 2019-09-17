from JSONParse import JSONText
import requests

class Weather:

    weather_endpoint = 'https://api.openweathermap.org/data/2.5/'

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.dict = self.GetWeather()['weather'][0]
        self.forecast = self.dict['main']
        print(self.forecast
              )
    def GetWeather(self):
        weather_query_response = self.APIRequest()
        weather_query_dicts = JSONText(weather_query_response.text).dict
        return weather_query_dicts

    def QueryString(self):
        file = open(".weather_config.txt", "r")
        weather_secret = file.read()
        return '/weather?lat=' + str(self.latitude) + '&lon=' + str(self.longitude) + '&appid=' + weather_secret

    def APIRequest(self):
        return requests.get(self.weather_endpoint + self.QueryString())

    def __str__(self):
        return self.forecast
