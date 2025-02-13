from transportQuery import PostcodeQuery
from transportQuery import BusStopQuery
from BusStop import BusStop
from JSONParse import JSONText

def main():
    bus_endpoint = 'https://transportapi.com/v3/uk/bus/stop/'
    stop_endpoint = "http://transportapi.com/v3/uk/"
    postcode_endpoint = 'https://api.postcodes.io/postcodes/'
    # weather_endpoint = 'https://api.openweathermap.org/data/2.5/'

    postcode = str(input("Enter your postcode: "))
    postcode_dict = PostcodeQuery.GetPostcodeInfo(postcode, postcode_endpoint)

    post_long = postcode_dict['longitude']
    post_lat = postcode_dict['latitude']

    list_bus_stops = BusStop.GetBusStops(post_lat, post_long, stop_endpoint)

    # PrintInfo(list_bus_stops, bus_endpoint)

# def PrintInfo(list_bus_stops, bus_endpoint):
#     print('Nearest bus stop')
#     list_bus_stops[0].GetBuses(bus_endpoint)
#     list_bus_stops[0].PrintBuses()
#     print('2nd Nearest bus stop')
#     list_bus_stops[1].GetBuses(bus_endpoint)
#     list_bus_stops[1].PrintBuses()





if __name__ == "__main__":
    main()