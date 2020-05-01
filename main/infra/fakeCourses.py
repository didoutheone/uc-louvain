from main.common.dto.courseData import CourseData
from main.courseGen.model.description import Description
from main.courseGen.model.volume import Volume
from main.courseGen.use_case.courses import Courses
from main.infra.io import Io

class FakeCourses(Courses):

    file_courses = "/home/clementine/Documents/Soat/formation_ddd/uc-louvain/db/courses"

    def getCourses(self):
        return Io.read(self.file_courses)

    def getCourseById(self, courseId):
        courses = self.getCourses()
        for course in courses['courses']:
            if course['id'] == courseId:
                return CourseData(courseId , course['teacher'], course['descriptions'], course['volumes'])

    def addCourse(self, course):
        data = self.createData(course)
        Io.write(self.file_courses, 'courses', data)

    def createData(self, course):
        descriptions = Description(course.descriptions.contenu, course.descriptions.acquis, course.descriptions.methode_evaluation).getSerializedDescriptions()
        volumes = Volume(course.volumes.magistraux, course.volumes.pratique).getSerializedVolumes()
        return {"id": course.courseId, "faculty": course.profilId.faculty, "teacher": course.profilId.profilId, "descriptions": descriptions,
                "volumes": volumes}



