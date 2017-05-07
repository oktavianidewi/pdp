import csv
import datetime

class Seeder():
    def __init__(self, filename):
        self.filename = filename

    def csv_file(self):
        readcsvfile = open(self.filename, 'rb')
        data = csv.reader(readcsvfile)
        header = next(data)
        # header.append('timestamp')

        dict_data = []
        for row in data:
            # row.append(datetime.datetime.now().strftime('%s'))
            # dict_data.append(dict(zip(header, row)))
            dict_data.append(row)
        return dict_data