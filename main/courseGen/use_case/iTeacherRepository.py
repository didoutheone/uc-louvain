from main.courseGen.use_case.teacherRepository import TeacherRepository


class ITeacherRepository():

    def canCreateCourse(self, idCourse, profilId):
        return TeacherRepository().canCreateCourse(idCourse, profilId)

    def getTeachers(self):
        return TeacherRepository().getTeachers()

    def addTeacher(self, teacher):
        return TeacherRepository().addTeacher(teacher)

    def findTeacherById(self, id):
        return TeacherRepository().findTeacherById(id)