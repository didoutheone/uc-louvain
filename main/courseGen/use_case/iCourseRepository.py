from main.courseGen.use_case.courseRepository import CourseRepository

class ICourseRepository:
    def getCourses(self):
        return CourseRepository().getCourses()

    def addCourse(self, course):
        return CourseRepository().addCourse(course)

    def getCourseById(self, profilId):
        return CourseRepository().getCourseById(profilId)