from main.common.dto.teacherData import TeacherData
from main.courseGen.exposition.displayCourse import DisplayCourse
from main.courseGen.exposition.generatorRequest import GeneratorRequest
from main.courseGen.model.course import Course
from main.courseGen.model.description import Description
from main.courseGen.model.idGenerator import IdGenerator
from main.courseGen.model.volume import Volume
from main.infra.fakeCourses import FakeCourses
from main.courseGen.use_case.generateCourse import GenerateCourse
from main.courseGen.use_case.teachers import Teachers

if __name__ == "__main__":
    # profilId = 1
    # descriptions = Description("du droit", "test2", "gros exam")
    # volumes = Volume(20, 5)
    # request = GeneratorRequest(profilId, descriptions, volumes)
    # generator = GenerateCourse(request, FakeCourses())
    # generator.generate()
    data = DisplayCourse('LDROI1623').displayCourse()
    print(data)