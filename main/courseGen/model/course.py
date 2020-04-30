from main.courseGen.model.exceptions.teacherCannotCreateCourse import TeacherCannotCreateCourse
from main.courseGen.model.teacher import Teacher

# titre unique a l'année et obligatoire
# nb crédit obl et > 0.
# quadrimestre val Q1 Q2 Q1&Q2
# cours externe commence par E - indiquer l'institution dans laquelle le cours se déroule
from main.courseGen.use_case.iTeacherRepository import ITeacherRepository
from main.courseGen.use_case.teacherRepository import TeacherRepository


class Course:

    def __init__(self, request):
        self.id = request.courseId
        self.profilId = request.profilId
        self.descriptions = request.descriptions
        self.volumes = request.volumes
        self.status = "uncreated"
        self.faculty = self.getFaculty()

    def createCourse(self):
        if not ITeacherRepository().canCreateCourse(self.id, self.profilId):
            raise TeacherCannotCreateCourse()
        self.status = "created"
        return self

    def getFaculty(self):
        teacher = TeacherRepository().findTeacherById(self.profilId)
        return teacher.faculty

    def getStatus(self):
        return self.status

    def setVolumesHoraires(self, volumes):
        self.volumes = volumes

    def setDescriptions(self, descriptions):
        self.descriptions = descriptions

    def getId(self):
        return self.id
