from main.common.dto.courseData import CourseData
from main.model.exceptions.teacherCannotCreateCourse import TeacherCannotCreateCourse
from main.model.idGenerator import IdGenerator
from main.infra.fakeTeachers import FakeTeachers

#Aggregate Root
class Course:

    def __init__(self, request, teacherData):
        self.courseId = None
        self.teacher = teacherData.getTeacher()
        self.descriptions = request.descriptions
        self.volumes = request.volumes
        self.status = "uncreated"
        self.faculty = self.getFaculty()

    def equals(self, course):
        return self.courseId == course.courseId

    def createCourse(self):
        self.courseId = IdGenerator().create_course_unique_id(self.teacher.faculty)
        if not self.teacher.canCreateCourse(self.courseId):
            raise TeacherCannotCreateCourse()
        self.status = "created"
        return self

    def getFaculty(self):
        teacher = FakeTeachers().findTeacherById(self.teacher.profilId)
        return teacher.faculty

    def getStatus(self):
        return self.status

    def setVolumesHoraires(self, volumes):
        self.volumes = volumes

    def setDescriptions(self, descriptions):
        self.descriptions = descriptions

    def getId(self):
        return self.courseId

    def getCourseData(self):
        return CourseData(self.courseId, self.teacher, self.descriptions, self.volumes)
