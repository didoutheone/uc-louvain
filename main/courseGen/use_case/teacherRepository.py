from main.infra.dbUtils import DbUtils


class TeacherRepository:

    teachers = DbUtils.read("/home/clementine/Documents/Soat/formation_ddd/uc-louvain/db/teachers")
    file = "/home/clementine/Documents/Soat/formation_ddd/uc-louvain/db/teachers"

    def findTeacherById(self, id):
        for teacher in self.teachers:
            if teacher.id == id:
                return teacher

    def addTeacher(self, teacher):
        data = self.createData(teacher)
        DbUtils.write(self.file, data)

    def createData(self, teacher):
        return {"id": teacher.id, "faculty": teacher.faculty}


