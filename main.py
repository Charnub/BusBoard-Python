# import json
# import requests
from transportQuery import BusQuery
from transportQuery import PostcodeQuery
from JSONParse import JSONText
def main():
    postcode_endpoint = 'https://api.postcodes.io/postcodes/'
    postcode = "BA1 1AN"
    postcodeQuery = PostcodeQuery(postcode_endpoint, postcode)
    postcode_response = postcodeQuery.Request()

    #print(type(postcode_response.text))
    postcode_json = JSONText(postcode_response.text).dict
    print(postcode_json['longitude'], postcode_json['latitude'])

    bus_stop_url = "http://transportapi.com/v3/uk/places.json?app_id=06c96df7&app_key=2927c9980ab1aec88eebede64029c064&lat=51.534121&lon=-0.006944&type=bus_stop"
    # chooseBus = input("Please enter a bus code: ")
    api_url = 'https://transportapi.com/v3/uk/bus/stop/'

    query = BusQuery(chooseBus, api_url)

    transport_response = query.Request()

    JSONText(transport_response)


if __name__ == "__main__":
    main()