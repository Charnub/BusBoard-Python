from transportQuery import PostcodeQuery
from transportQuery import BusStopQuery
from BusStop import BusStop
from JSONParse import JSONText

def main():
    bus_endpoint = 'https://transportapi.com/v3/uk/bus/stop/'
    stop_endpoint = "http://transportapi.com/v3/uk/"
    postcode_endpoint = 'https://api.postcodes.io/postcodes/'

    postcode = str(input("Enter your postcode: "))
    postcode_dict = GetPostcodeInfo(postcode, postcode_endpoint)

    post_long = postcode_dict['longitude']
    post_lat = postcode_dict['latitude']

    weather_api = "api.openweathermap.org/data/2.5/weather?lat=" + str(post_lat) + "&lon=" + str(post_long) + "&appid=e34b03caaeef821f7d7a0724b32de446"
    print(weather_api)

    list_bus_stops = GetBusStops(post_lat, post_long, stop_endpoint)

    PrintInfo(list_bus_stops, bus_endpoint)


def PrintInfo(list_bus_stops, bus_endpoint):
    print('Nearest bus stop')
    list_bus_stops[0].GetBuses(bus_endpoint)
    list_bus_stops[0].PrintBuses()
    print('2nd Nearest bus stop')
    list_bus_stops[1].GetBuses(bus_endpoint)
    list_bus_stops[1].PrintBuses()


def GetBusStops(post_lat, post_long, stop_endpoint):

    bus_stop_query = BusStopQuery(stop_endpoint, post_long, post_lat)
    bus_stop_response = bus_stop_query.Request()
    bus_stop_dicts = JSONText(bus_stop_response.text).dict['member']  # list of dicts

    list_bus_stops = BusStop.GetStops(bus_stop_dicts)

    return list_bus_stops


def GetPostcodeInfo(postcode, postcode_endpoint):

    postcodeQuery = PostcodeQuery(postcode_endpoint, postcode)
    postcode_response = postcodeQuery.Request()
    postcode_dict = JSONText(postcode_response.text).dict['result']

    return postcode_dict


if __name__ == "__main__":
    main()