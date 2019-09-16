from flask import Flask, render_template, request
from transportQuery import PostcodeQuery
from transportQuery import BusStopQuery
from BusStop import BusStop
from JSONParse import JSONText
from main import GetBusStops, GetPostcodeInfo
app = Flask(__name__)

bus_endpoint = 'https://transportapi.com/v3/uk/bus/stop/'
stop_endpoint = "http://transportapi.com/v3/uk/"
postcode_endpoint = 'https://api.postcodes.io/postcodes/'

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/busInfo")
def busInfo():
    postcode = request.args.get('postcode')
    postcode_dict = GetPostcodeInfo(postcode, postcode_endpoint)

    post_long = postcode_dict['longitude']
    post_lat = postcode_dict['latitude']

    list_bus_stops = GetBusStops(post_lat, post_long, stop_endpoint)


    for stop in list_bus_stops:
        stop.GetBuses(bus_endpoint)

    buses = list_bus_stops[0].buses

    [bus_numbers, bus_directions, bus_departures] = [[], [], []]
    for bus in buses:
        bus_numbers.append(bus.line_name)
        bus_directions.append(bus.direction)
        bus_departures.append(bus.dep_time)

    print(bus_directions)
    print(bus_departures)

    return render_template('info.html', postcode=postcode, stop=list_bus_stops[0].name, bus=bus_numbers, direction=bus_directions, departure=bus_departures)

if __name__ == "__main__": app.run()