import random
from main.infra.fakeCourses import FakeCourses
from main.infra.fakePartims import FakePartims


class IdGenerator():

    def create_course_unique_id(self, faculty):
        id = (faculty + "DROI") + str(random.randint(1000, 9999))
        if FakeCourses().getCourseById(id):
            self.create_course_unique_id(faculty)
        return id

    def create_partim_unique_id(self, courseId):
        alph = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        for i in alph:
            partimId = courseId + i
            if not FakePartims().getPartimById(partimId):
                return partimId
