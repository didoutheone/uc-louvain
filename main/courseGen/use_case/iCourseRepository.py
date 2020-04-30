from main.courseGen.use_case.courseRepository import CourseRepository

class ICourseRepository:
    def getCourses(self):
        CourseRepository().getCourses()

    def addCourse(self, course):
        CourseRepository().addCourse(course)