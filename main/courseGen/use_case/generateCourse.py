from main.courseGen.model.idGenerator import IdGenerator
from main.courseGen.exposition.generatorResponse import GeneratorResponse
from main.courseGen.model.course import Course
from main.courseGen.use_case.courseRepository import CourseRepository
from main.courseGen.use_case.teacherRepository import TeacherRepository


class GenerateCourse:

    def __init__(self, profilId, descriptions, volume):
        self.course = None
        self.id = None
        self.profilID = profilId
        self.descriptions = descriptions
        self.volume = volume

    def generate(self, request):
        self.id = IdGenerator().create_unique_id()
        teacher = TeacherRepository().findTeacherById(request.profilId)
        course = Course(id, teacher)
        course.createCourse()
        #transformer en course data
        response = GeneratorResponse(course)

        #Appel course data pour persistence
        CourseRepository().addCourse(response.course)
        #DisplayCourse()
        #return response