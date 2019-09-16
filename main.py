import json
import requests

def main():
    chooseBus = input("Please enter a bus code: ")
    response = requests.get('https://transportapi.com/v3/uk/bus/stop/'+chooseBus+'/live.json?app_id=06c96df7&app_key=2927c9980ab1aec88eebede64029c064&group=route&nextbuses=no')
    test = response.text
    parsedJSON = json.loads(test)
    print(json.dumps(parsedJSON, indent=4))


if __name__ == "__main__":
    main()