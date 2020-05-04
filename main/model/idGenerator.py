import random
from main.infra.fakeCourses import FakeCourses

# Domain Service
class IdGenerator():

    def create_unique_id(self, faculty):
        id = (faculty + "DROI") + str(random.randint(1000, 9999))
        if FakeCourses().getCourseById(id):
            self.create_unique_id(faculty)
        return id