from main.common.dto.teacherData import TeacherData
from main.courseGen.model.exceptions.alreadyExistingTeacher import AlreadyExistingTeacher
from main.courseGen.use_case.teachers import Teachers
from main.infra.io import Io


class FakeTeachers(Teachers):

    file_teachers = "/home/clementine/Documents/Soat/formation_ddd/uc-louvain/db/teachers"

    def getTeachers(self):
        return Io.read(self.file_teachers)

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
                Io.write(self.file_teachers, 'teachers', data)
            else:
                raise AlreadyExistingTeacher()

    def createData(self, teacher):
        return {"id": teacher.id, "faculty": teacher.faculty}


