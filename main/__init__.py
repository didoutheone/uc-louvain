from main.common.dto.teacherData import TeacherData
from main.courseGen.exposition.generatorRequest import GeneratorRequest
from main.courseGen.model.course import Course
from main.courseGen.model.description import Description
from main.courseGen.model.idGenerator import IdGenerator
from main.courseGen.model.volume import Volume
from main.courseGen.use_case.generateCourse import GenerateCourse
from main.courseGen.use_case.iTeacherRepository import ITeacherRepository

if __name__ == "__main__":

    profilId = 1
    teacher = ITeacherRepository().findTeacherById(profilId)
    courseId = IdGenerator().create_unique_id(teacher.faculty)
    descriptions = Description("du droit", "plus de droit", "gros exam")
    volumes = Volume(20, 5)
    request = GeneratorRequest(profilId, courseId, descriptions, volumes)
    generator = GenerateCourse(request)
    generator.generate()
    print('test')