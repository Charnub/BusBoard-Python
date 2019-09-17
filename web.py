from flask import Flask, render_template, request
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

    # bus_stop_1 = list_bus_stops[0].buses
    # bus_stop_2 = list_bus_stops[1].buses
    #
    # [bus_numbers_1, bus_directions_1, bus_departures_1] = [[], [], []]
    # for bus in bus_stop_1:
    #     bus_numbers_1.append(bus.line_name)
    #     bus_directions_1.append(bus.direction)
    #     bus_departures_1.append(bus.dep_time)
    #
    # [bus_numbers_2, bus_directions_2, bus_departures_2] = [[], [], []]
    # for bus in bus_stop_2:
    #     bus_numbers_2.append(bus.line_name)
    #     bus_directions_2.append(bus.direction)
    #     bus_departures_2.append(bus.dep_time)


    return render_template('info.html', postcode=postcode, stops=list_bus_stops)


if __name__ == "__main__":
    app.run()