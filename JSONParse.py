import json

class JSONText:
    def __init__(self, response):
        self.file = response
        self.dict = json.loads(response)

