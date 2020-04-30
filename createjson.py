import json

if __name__ == "__main__":
    file = "/home/clementine/Documents/Soat/formation_ddd/uc-louvain/db/teachers"

    with open(file, 'w') as outfile:
         data = {}
         data['teachers'] = []
         json.dump(data, outfile)

    with open(file) as json_file:
         data = json.load(json_file)
         print(data)