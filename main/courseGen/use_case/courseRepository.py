from main.courseGen.model.description import Description
from main.courseGen.model.volume import Volume
from main.infra.dbUtils import DbUtils

class CourseRepository:

    file_courses = "/home/clementine/Documents/Soat/formation_ddd/uc-louvain/db/courses"

    def getCourses(self):
        DbUtils.read(self.file_courses)

    def addCourse(self, course):
        data = self.createData(course)
        DbUtils.write(self.file_courses, 'courses', data)

    def createData(self, course):
        descriptions = Description(course.descriptions.contenu, course.descriptions.acquis, course.descriptions.methode_evaluation).getSerializedDescriptions()
        volumes = Volume(course.volumes.magistraux, course.volumes.pratique).getSerializedVolumes()
        return {"id": course.id, "faculty": course.faculty, "teacher": course.profilId, "descriptions": descriptions,
                "volumes": volumes}


