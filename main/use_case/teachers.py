import abc

class Teachers():

    @abc.abstractmethod
    def canCreateCourse(self, idCourse, profilId):
        pass

    @abc.abstractmethod
    def getTeachers(self):
        pass

    @abc.abstractmethod
    def addTeacher(self, teacher):
        pass

    @abc.abstractmethod
    def findTeacherById(self, profilId):
        pass