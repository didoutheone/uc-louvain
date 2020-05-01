from main.common.dto.teacherData import TeacherData
from main.infra.dbUtils import DbUtils


class TeacherRepository:

    file_teachers = "/home/clementine/Documents/Soat/formation_ddd/uc-louvain/db/teachers"

    def getTeachers(self):
        return DbUtils.read(self.file_teachers)

    def findTeacherById(self, profilId):
        teachers = self.getTeachers()
        for teacher in teachers['teachers']:
            if teacher['id'] == profilId:
                found = TeacherData(profilId, teacher['faculty'])
                return found

    def addTeacher(self, teacher):
        data = self.createData(teacher)
        teachers = self.getTeachers()
        for existingTeacher in teachers['teachers']:
            if existingTeacher['id'] != teacher.id:
                DbUtils.write(self.file_teachers,'teachers', data)
            else:
                print("NON")

                #TODO raise erreur

    def createData(self, teacher):
        return {"id": teacher.id, "faculty": teacher.faculty}


