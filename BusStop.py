from transportQuery import BusQuery
from JSONParse import JSONText


class BusStop:
    def __init__(self, name, atco, distance):
        self.atco = atco
        self.name = name
        self.distance = distance
        self.buses = []


    @staticmethod
    def GetStops(bus_dicts):
        stopList = []
        for i in range(0, len(bus_dicts)):
            dict = bus_dicts[i]
            stopList.append(BusStop(dict['name'], dict['atcocode'], dict['distance']))
        return stopList

    def GetBuses(self, bus_api):
        query = BusQuery(self.atco, bus_api)
        bus_query = query.Request().text
        busInfoDict = JSONText(bus_query).dict['departures']
        keys = busInfoDict.keys()
        # print(busInfoDict)
        for key in keys:
            for dict in busInfoDict[key]:
                bus = Bus(self.name, dict['line'], dict['direction'], dict['aimed_departure_time'])
                self.buses.append(bus)

    def __str__(self):
        return self.name

    def PrintBuses(self):
        for bus in self.buses:
            print(bus)

class Bus:
    def __init__(self, stop_name, line_name, direction, dep_time):
        self.line_name = line_name
        self.stop_name = stop_name
        self.direction = direction
        self.dep_time = dep_time

    def __str__(self):
        return f"""
        Bus Stop: {self.stop_name}
        Bus No: {self.line_name} towards {self.direction}
        Expected at: {self.dep_time}
"""
        #return self.stop_name + " - Bus No: " + self.line_name + ' towards ' + self.direction + ' expected at ' + self.dep_time