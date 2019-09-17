from flask import Flask, render_template, request

import BusStop

from transportQuery import PostcodeQuery
from BusStop import BusStop
from weather import Weather

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
    postcode_dict = PostcodeQuery.GetPostcodeInfo(postcode, postcode_endpoint)

    post_long = postcode_dict['longitude']
    post_lat = postcode_dict['latitude']

    weather = Weather(post_lat, post_long)

    list_bus_stops = BusStop.GetBusStops(post_lat, post_long, stop_endpoint)

    for stop in list_bus_stops:
        stop.GetBuses(bus_endpoint)

    return render_template('info.html', postcode=postcode, stops=list_bus_stops, weather=weather.forecast)


if __name__ == "__main__":
    app.run()
