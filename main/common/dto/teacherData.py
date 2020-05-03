from main.model.teacher import Teacher


class TeacherData:
    def __init__(self, id, faculty):
        self.id = id
        self.faculty = faculty

    def getFaculty(self):
        return self.faculty

    def getId(self):
        return self.id

    def getTeacher(self):
        return Teacher(self.id, self.faculty)

