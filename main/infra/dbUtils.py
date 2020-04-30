import json

class DbUtils:

    def read(file):
        with open(file) as json_file:
            return json.load(json_file)

    def write(file, object):
        with open(file, 'w+') as outfile:
            data = json.load(outfile)
            data['teachers'].append(object)
            json.dump(data, outfile)