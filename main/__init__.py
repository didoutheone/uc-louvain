from main.common.dto.teacherData import TeacherData
from main.courseGen.use_case.teacherRepository import TeacherRepository

if __name__ == "__main__":
    teacher = TeacherData(1, "UugeiuCL")
    file = "/home/clementine/Documents/Soat/formation_ddd/uc-louvain/db/teachers"
    teacherrep = TeacherRepository().addTeacher(teacher)
