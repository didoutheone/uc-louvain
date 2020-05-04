import abc

# epository
class Courses:

    @abc.abstractmethod
    def getCourses(self):
        pass

    @abc.abstractmethod
    def addCourse(self, course):
        pass

    @abc.abstractmethod
    def getCourseById(self, id):
        pass