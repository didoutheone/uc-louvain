from main.common.dto.courseData import CourseData
from main.courseGen.model.exceptions.teacherCannotCreateCourse import TeacherCannotCreateCourse
from main.courseGen.model.idGenerator import IdGenerator
from main.courseGen.model.teacher import Teacher

# titre unique a l'année et obligatoire
# nb crédit obl et > 0.
# quadrimestre val Q1 Q2 Q1&Q2
# cours externe commence par E - indiquer l'institution dans laquelle le cours se déroule
from main.courseGen.use_case.teacherRepository import TeacherRepository

#Aggregate Root
class Course:

    def __init__(self, request, teacherData):
        self.courseId = None
        self.teacher = teacherData.getTeacher()
        self.descriptions = request.descriptions
        self.volumes = request.volumes
        self.status = "uncreated"
        self.faculty = self.getFaculty()

    def createCourse(self):
        self.courseId = IdGenerator().create_unique_id(self.teacher.faculty)
        if not self.teacher.canCreateCourse(self.courseId):
            raise TeacherCannotCreateCourse()
        self.status = "created"
        return self

    def getFaculty(self):
        teacher = TeacherRepository().findTeacherById(self.teacher.profilId)
        return teacher.faculty

    def getStatus(self):
        return self.status

    def setVolumesHoraires(self, volumes):
        self.volumes = volumes

    def setDescriptions(self, descriptions):
        self.descriptions = descriptions

    def getId(self):
        return self.courseId

    def getCourseData(self):
        return CourseData(self.courseId, self.teacher, self.descriptions, self.volumes)
