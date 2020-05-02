from main.common.dto.teacherData import TeacherData
from main.exposition.courseCreationRequest import CourseCreationRequest
from main.model.course import Course
from main.model.description import Description
from main.model.volume import Volume
from main.infra.fakeCourses import FakeCourses
from main.use_case.createCourse import CreateCourse

if __name__ == "__main__":
     profilId = 1
     descriptions = Description("Introduction au droit", "Code du travail", "TP et examen")
     volumes = Volume(60, 10)
     request = CourseCreationRequest(profilId, descriptions, volumes)
     courseCreator = CreateCourse(request, FakeCourses())
     courseCreator.create()
    #data = DisplayCourse('LDROI1623').displayCourse()
    #print(data)