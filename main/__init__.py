from main.common.dto.teacherData import TeacherData
from main.courseGen.exposition.displayCourse import DisplayCourse
from main.courseGen.exposition.courseCreationRequest import CourseCreationRequest
from main.courseGen.model.course import Course
from main.courseGen.model.description import Description
from main.courseGen.model.idGenerator import IdGenerator
from main.courseGen.model.volume import Volume
from main.infra.fakeCourses import FakeCourses
from main.courseGen.use_case.createCourse import CreateCourse
from main.courseGen.use_case.teachers import Teachers

if __name__ == "__main__":
     profilId = 1
     descriptions = Description("du droit", "test2", "gros exam")
     volumes = Volume(0, 0)
     request = CourseCreationRequest(profilId, descriptions, volumes)
     courseCreator = CreateCourse(request, FakeCourses())
     courseCreator.create()
    #data = DisplayCourse('LDROI1623').displayCourse()
    #print(data)