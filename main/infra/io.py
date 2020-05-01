import json

class Io:

    def read(file):
        outfile = open(file)
        data = json.load(outfile)
        outfile.close()
        return data

    def write(file, str, object):
        data = Io.read(file)
        outfile = open(file, 'w')
        data[str].append(object)
        json.dump(data, outfile)
        outfile.close()
