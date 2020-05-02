from main.common.dto.partimData import PartimData
from main.infra.fakeCourses import FakeCourses
from main.model.exceptions.partimCannotBeCreatedError import PartimCannotBeCreatedError
from main.model.idGenerator import IdGenerator


class Partim:
    def __init__(self, request, teacherData):
        self.course = FakeCourses().getCourseById(request.courseId)
        self.intitule = request.intitule
        self.partimId = None
        self.teacherData = teacherData
        self.status = "uncreated"

    def createPartim(self):
        if not self.course or self.course.profilId != self.teacherData.profilId:
            raise PartimCannotBeCreatedError
        self.partimId = IdGenerator().create_partim_unique_id(self.course.courseId)
        self.status = "created"
        return self

    def getPartimData(self):
        return PartimData(self.partimId, self.course.courseId, self.intitule)