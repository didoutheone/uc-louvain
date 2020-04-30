import json

class DbUtils:

    def read(file):
        outfile = open(file)
        data = json.load(outfile)
        outfile.close()
        return data

    def write(file, object):
        data = DbUtils.read(file)
        outfile = open(file, 'w')
        data['teachers'].append(object)
        json.dump(data, outfile)
        outfile.close()
