from main.courseGen.model.exceptions.teacherCannotCreateCourse import TeacherCannotCreateCourse
from main.courseGen.model.teacher import Teacher

# titre unique a l'année et obligatoire
# nb crédit obl et > 0.
# quadrimestre val Q1 Q2 Q1&Q2
# cours externe commence par E - indiquer l'institution dans laquelle le cours se déroule


class Course:

    def __init__(self, id, teacher):
        self.id = id
        self.faculty = teacher.faculty
        self.teachers = teacher
        self.descriptions = None
        self.volumesHoraires = None
        self.status = "uncreated"

    def createCourse(self):
        self.teacher = Teacher().canCreateCourse(self.id)
        if not self.teachers:
            raise TeacherCannotCreateCourse()
        self.status = "created"
        return self

    def getStatus(self):
        return self.status

    def setVolumesHoraires(self, volumes):
        self.volumes = volumes

    def setDescriptions(self, descriptions):
        self.descriptions = descriptions

    def getId(self):
        return self.id

