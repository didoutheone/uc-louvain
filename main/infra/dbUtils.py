import json

class DbUtils:

    def read(file):
        outfile = open(file)
        data = json.load(outfile)
        outfile.close()
        return data

    def write(file, str, object):
        data = DbUtils.read(file)
        outfile = open(file, 'w')
        data[str].append(object)
        json.dump(data, outfile)
        outfile.close()
