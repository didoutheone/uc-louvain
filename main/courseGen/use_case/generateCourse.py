from main.courseGen.model.idGenerator import IdGenerator
from main.courseGen.exposition.generatorResponse import GeneratorResponse
from main.courseGen.model.course import Course
from main.courseGen.use_case.iCourseRepository import ICourseRepository


class GenerateCourse:

    def __init__(self, request):
        self.request = request

    def generate(self):
        course = Course(self.request)
        course = course.createCourse()
        #transformer en course data
        response = GeneratorResponse(course)
        #Appel course data pour persistence
        ICourseRepository().addCourse(response.course)
        #DisplayCourse()
        #return response

    #def canBeGenerated(self):
