import requests
from JSONParse import JSONText

class BusQuery:
    def __init__(self, chooseBus, api_url, limit = 5, next_buses = "no"):
        file = open(".config.txt", "r")
        secret = file.read()
        [self.app_id, self.app_key] = secret.split()
        self.chooseBus = chooseBus
        self.api_url = api_url
        self.limit = str(limit)
        self.next_buses = next_buses
        self.queryParameters = '/live.json?app_id=' + self.app_id +'&app_key=' + self.app_key + '&group=route&limit=' + self.limit + '&nextbuses=' + self.next_buses

    def Request(self):
        return requests.get(self.api_url + self.chooseBus + self.queryParameters)

class BusStopQuery:
    def __init__(self, bus_stop_url, longitude, latitude, type="bus_stop"):
        file = open(".config.txt", "r")
        secret = file.read()
        [self.app_id, self.app_key] = secret.split()
        self.bus_stop_url = bus_stop_url
        self.longitude = longitude
        self.latitude = latitude
        self.type = type
        self.queryParameters = '/places.json?app_id=' + self.app_id + '&app_key=' + self.app_key + '&lat=' + str(self.latitude) + '&lon=' + str(self.longitude) + '&type=' + self.type

    def Request(self):
        return requests.get(self.bus_stop_url + self.queryParameters)


class PostcodeQuery:
    def __init__(self, postcode_endpoint, postcode):
        self.postcode_endpoint = postcode_endpoint
        self.postcode = postcode

    def Request(self):
        return requests.get(self.postcode_endpoint + self.postcode)

    @staticmethod
    def GetPostcodeInfo(postcode, postcode_endpoint):
        postcodeQuery = PostcodeQuery(postcode_endpoint, postcode)
        postcode_response = postcodeQuery.Request()
        postcode_dict = JSONText(postcode_response.text).dict['result']

        return postcode_dict






# class WeatherQuery:
#     def __init__(self, weather_endpoint, latitude, longitude):
#         file = open(".weather_config.txt", "r")
#         weather_secret = file.read()
#         self.weather_endpoint = weather_endpoint
#         self.latitude = latitude
#         self.longitude = longitude
#         self.api_key = weather_secret
#         self.queryParameters = '/weather?lat=' + str(self.latitude) + '&lon=' + str(self.longitude) + '&appid=' + self.api_key
#
#     def Request(self):
#         return requests.get(self.weather_endpoint + self.queryParameters)