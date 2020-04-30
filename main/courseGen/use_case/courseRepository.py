from main.infra.dbUtils import DbUtils

class CourseRepository:

    def getCourses(self):
        pass

    def addCourse(self):
        DbUtils.write(self.file, self.createData())

    def createData(self):
        return {"id": self.id, "faculty": self.faculty, "teachers": self.teachers, "descriptions": self.descriptions,
                "volumes": self.volumes}


