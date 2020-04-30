from main.infra.dbUtils import DbUtils


class TeacherRepository:

    file_teachers = "/home/clementine/Documents/Soat/formation_ddd/uc-louvain/db/teachers"

    def getTeachers(self):
        return DbUtils.read(self.file_teachers)

    def findTeacherById(self, id):
        for teacher in self.getTeachers():
            if teacher.id == id:
                return teacher

    def addTeacher(self, teacher):
        data = self.createData(teacher)
        DbUtils.write(self.file_teachers, data)

    def createData(self, teacher):
        return {"id": teacher.id, "faculty": teacher.faculty}


