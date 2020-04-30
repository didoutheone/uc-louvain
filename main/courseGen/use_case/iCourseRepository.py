from main.courseGen.use_case.courseRepository import CourseRepository


class ICourseRepository:
    def getCourses(self):
        CourseRepository().getCourses()