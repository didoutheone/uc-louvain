from main.courseGen.model.course import Course
from main.courseGen.use_case.iCourseRepository import ICourseRepository
from main.courseGen.use_case.iTeacherRepository import ITeacherRepository


class GenerateCourse:

    def __init__(self, request):
        self.request = request
        self.course = None
        self.courseData = None

    def generate(self):
        teacherData = ITeacherRepository().findTeacherById(self.request.profilId)
        self.course = Course(self.request, teacherData)
        self.course = self.course.createCourse()
        self.courseData = self.course.getCourseData()
        ICourseRepository().addCourse(self.courseData)