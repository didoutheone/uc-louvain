class Teacher:
    def __init__(self, profilId, faculty):
        self.profilId = profilId
        self.faculty = faculty

    def canCreateCourse(self, idCourse):
        if self.faculty == idCourse[0]:
            return True
        return False