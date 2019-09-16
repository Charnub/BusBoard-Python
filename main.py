from transportQuery import BusQuery
from transportQuery import PostcodeQuery
from transportQuery import BusStopQuery
from BusStop import BusStop
from JSONParse import JSONText
def main():
    postcode_endpoint = 'https://api.postcodes.io/postcodes/'
    postcode = str(input("Enter your postcode: "))
    # postcode = "BA1 1AN"
    postcodeQuery = PostcodeQuery(postcode_endpoint, postcode)
    postcode_response = postcodeQuery.Request()
    postcode_dict = JSONText(postcode_response.text).dict['result']

    post_long = postcode_dict['longitude']
    post_lat = postcode_dict['latitude']

    bus_stop_url = "http://transportapi.com/v3/uk/"
    bus_stop_query = BusStopQuery(bus_stop_url, post_long, post_lat)
    bus_stop_response = bus_stop_query.Request()
    bus_stop_dicts = JSONText(bus_stop_response.text).dict['member'] # list of dicts
    # print(bus_stop_dicts)

    bus_api_url = 'https://transportapi.com/v3/uk/bus/stop/'

    list_bus_stops = BusStop.GetStops(bus_stop_dicts)
    print('Nearest bus stop')
    list_bus_stops[0].GetBuses(bus_api_url)
    list_bus_stops[0].PrintBuses()
    print('2nd Nearest bus stop')
    list_bus_stops[1].GetBuses(bus_api_url)
    list_bus_stops[1].PrintBuses()
    # print(list_bus_stops[0].buses)
    # bus_info = list_bus_stops[0].GetBuses(bus_api_url)
    # print(bus_info)
    # for stop in list_bus_stops:
    #     print(stop)



    # chooseBus
    # api_url = 'https://transportapi.com/v3/uk/bus/stop/'
    #
    # query = BusQuery(chooseBus, api_url)
    #
    # transport_response = query.Request()
    #
    # JSONText(transport_response)


if __name__ == "__main__":
    main()