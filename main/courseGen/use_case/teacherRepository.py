from main.common.dto.teacherData import TeacherData
from main.infra.dbUtils import DbUtils


class TeacherRepository:

    file_teachers = "/home/clementine/Documents/Soat/formation_ddd/uc-louvain/db/teachers"

    def getTeachers(self):
        return DbUtils.read(self.file_teachers)

    def findTeacherById(self, id):
        teachers = self.getTeachers()
        for teacher in teachers['teachers']:
            if teacher['id'] == id:
                found = TeacherData(id, teacher['faculty'])
                return found

    def addTeacher(self, teacher):
        data = self.createData(teacher)
        teachers = self.getTeachers()
        for existingTeacher in teachers['teachers']:
            if existingTeacher['id'] != teacher.id:
                DbUtils.write(self.file_teachers,'teachers', data)
            else:
                print("NON")

    def canCreateCourse(self, idCourse, profilId):
        teacher = self.findTeacherById(profilId)
        test = idCourse[1:5]
        if teacher.faculty == idCourse[0]:
            return True
        return False

    def createData(self, teacher):
        return {"id": teacher.id, "faculty": teacher.faculty}


