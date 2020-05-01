from main.courseGen.model.course import Course
from main.infra.fakeTeachers import FakeTeachers


class GenerateCourse:

    def __init__(self, request, repository):
        self.request = request
        self.course = None
        self.courseData = None
        self.courseRepository = repository

    def generate(self):
        teacherData = FakeTeachers().findTeacherById(self.request.profilId)
        self.course = Course(self.request, teacherData)
        self.course = self.course.createCourse()
        self.courseData = self.course.getCourseData()
        self.courseRepository.addCourse(self.courseData)