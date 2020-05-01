from main.common.dto.teacherData import TeacherData
from main.exposition.displayCourse import DisplayCourse
from main.exposition.courseCreationRequest import CourseCreationRequest
from main.model.description import Description
from main.model.idGenerator import IdGenerator
from main.model.volume import Volume
from main.infra.fakeCourses import FakeCourses
from main.use_case.createCourse import CreateCourse
from main.use_case.teachers import Teachers

if __name__ == "__main__":
     profilId = 1
     descriptions = Description("du droit", "test2", "gros exam")
     volumes = Volume(0, 0)
     request = CourseCreationRequest(profilId, descriptions, volumes)
     courseCreator = CreateCourse(request, FakeCourses())
     courseCreator.create()
    #data = DisplayCourse('LDROI1623').displayCourse()
    #print(data)