class TeacherData:
    def __init__(self, id, faculty):
        self.id = id
        self.faculty = faculty
        self.file = "/home/clementine/Documents/Soat/formation_ddd/uc-louvain/db/teachers"

    def getFaculty(self):
        return self.faculty

    def getId(self):
        return self.id

