import json
import csv

class Cache(object):
    def __init__(self, filename):
        self.filename = filename

    # to store data to certain filename
    def store(self, obj):
        with open(self.filename, 'w') as file:
            file.write(json.dumps(obj))
            file.close()
        return True

    def update(self, id, obj):
        with open(self.filename, 'w') as file:
            file.write(json.dumps(obj))
            file.close()
        return True

    # to load the data from certain filename
    def load(self):
        with open(self.filename, 'r') as file:
            json_data = json.load(file)
            file.close()
        return json_data