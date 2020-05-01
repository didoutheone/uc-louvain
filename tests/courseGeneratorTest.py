import unittest

from main.exposition.displayCourse import DisplayCourse
from main.exposition.courseCreationRequest import CourseCreationRequest
from main.model.description import Description
from main.model.volume import Volume
from main.use_case.createCourse import CreateCourse
from main.infra.fakeCourses import FakeCourses


class GenerateCourseTest(unittest.TestCase):

    def test_generate_course(self):
        profilId = 1
        descriptions = Description("du droit", "test2", "gros exam")
        volumes = Volume(20, 5)
        request = CourseCreationRequest(profilId, descriptions, volumes)

        courseCreator = CreateCourse(request, FakeCourses())
        courseCreator.create()

        self.assertEqual(courseCreator.course.status, "created")

    def test_display_course(self):
        courseId = 'LDROI1623'
        expectedData = "Id cours : LDROI1623\nId professeur: 1\nDescription du cours :\n\tContenu : du droit\n\tAcquis : plus de droit\n\tMethode d'évaluation : gros exam\nVolumes horaires :\n\tCours magistraux : 20 heures\n\tTravaux pratiques : 5 heures\n"

        actual = DisplayCourse(courseId).displayCourse()

        self.assertEqual(actual, expectedData)

    # def test_should_not_generate_course(self):
    #     profilId = 1
    #     descriptions = Description(None, None, None)
    #     volumes = Volume(None, None)
    #     request = GeneratorRequest(profilId, descriptions, volumes)
    #     #
    #     # generator = GenerateCourse(request, FakeCourses())
    #     # generator.generate()
    #
    #
    #     self.assertRaises(GeneratorRequest(profilId, descriptions, volumes), CourseCannotBeCreated)
