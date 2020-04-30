from main.courseGen.use_case.teacherRepository import TeacherRepository


class ITeacherRepository():
    def findTeacherById(self, id):
        return TeacherRepository().findTeacherById(id)