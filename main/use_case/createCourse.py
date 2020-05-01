from main.common.events import mailEvent
from main.common.events.event import Event
from main.model.course import Course
from main.infra.fakeTeachers import FakeTeachers


class CreateCourse:

    def __init__(self, request, repository):
        self.request = request
        self.course = None
        self.courseData = None
        self.courseRepository = repository

    def create(self):
        teacherData = FakeTeachers().findTeacherById(self.request.profilId)
        self.course = Course(self.request, teacherData)
        self.course = self.course.createCourse()
        self.courseData = self.course.getCourseData()
        self.courseRepository.addCourse(self.courseData)
        if self.course.status == "created":
            event = Event()
            event += mailEvent.mailEvent
            event.notify(self.course.teacher.profilId, self.course.courseId, self.course.teacher.faculty)