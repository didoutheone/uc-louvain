from main.common.dto.teacherData import TeacherData
from main.exposition.courseCreationRequest import CourseCreationRequest
from main.exposition.displayPartim import DisplayPartim
from main.exposition.partimCreationRequest import PartimCreationRequest
from main.infra.fakePartims import FakePartims
from main.model.course import Course
from main.model.description import Description
from main.model.volume import Volume
from main.infra.fakeCourses import FakeCourses
from main.use_case.createCourse import CreateCourse
from main.use_case.createPartim import CreatePartim

if __name__ == "__main__":
     profilId = 1
     #descriptions = Description("Introduction au droit", "Code du travail", "TP et examen")
     #volumes = Volume(60, 10)
     courseId = "LDROI6775"
     partimId= "LDROI6775A"
     intitule = "Premiere partie du cours"
     #request = PartimCreationRequest(profilId, courseId, intitule)
     #partimCreator = CreatePartim(request, FakePartims())
     #partimCreator.create()
     data = DisplayPartim(partimId).displayPartim()
     print(data)