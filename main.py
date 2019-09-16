# import json
# import requests
from transportQuery import BusQuery
from transportQuery import PostcodeQuery
from transportQuery import BusStopQuery
from JSONParse import JSONText
def main():
    postcode_endpoint = 'https://api.postcodes.io/postcodes/'
    postcode = str(input("Enter your postcode: "))
    postcodeQuery = PostcodeQuery(postcode_endpoint, postcode)
    postcode_response = postcodeQuery.Request()
    postcode_dict = JSONText(postcode_response.text).dict['result']

    post_long = postcode_dict['longitude']
    post_lat = postcode_dict['latitude']

    bus_stop_url = "http://transportapi.com/v3/uk/"
    bus_stop_query = BusStopQuery(bus_stop_url, post_long, post_lat)
    bus_stop_response = bus_stop_query.Request()
    bus_stop_dicts = JSONText(bus_stop_response.text).dict['member'] # list of dicts
    atcocodes = []
    for i in range(0,len(bus_stop_dicts)):
        dict = bus_stop_dicts[i]
        atcocodes.append((dict['name'], dict['atcocode'], dict['distance']))
    print(atcocodes)
    # chooseBus = input("Please enter a bus code: ")
    # api_url = 'https://transportapi.com/v3/uk/bus/stop/'
    #
    # query = BusQuery(chooseBus, api_url)
    #
    # transport_response = query.Request()
    #
    # JSONText(transport_response)


if __name__ == "__main__":
    main()