from main.model.teacher import Teacher


class TeacherData:
    def __init__(self, profilId, faculty):
        self.profilId = profilId
        self.faculty = faculty

    def getFaculty(self):
        return self.faculty

    def getId(self):
        return self.profilId

    def getTeacher(self):
        return Teacher(self.profilId, self.faculty)

