import json

from main.common.dto.teacherData import TeacherData
from main.courseGen.use_case.teacherRepository import TeacherRepository
# from main.infra.dbUtils import DbUtils

if __name__ == "__main__":
    teacher = TeacherData(1, "UugeiuCL")
    file = "/home/clementine/Documents/Soat/formation_ddd/uc-louvain/db/teachers"
    teacherrep = TeacherRepository().addTeacher(teacher)


    # with open(file, 'w') as outfile:
    #      data = {}
    #      data['teachers'] = ["jhjkhk", "giughj"]
    #      json.dump(data, outfile)
    #
    # with open(file) as json_file:
    #      data = json.load(json_file)
    #      print(data)