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
        descriptions = Description("Introduction au droit", "Code du travail", "TP et examen")
        volumes = Volume(60, 10)
        request = CourseCreationRequest(profilId, descriptions, volumes)

        courseCreator = CreateCourse(request, FakeCourses())
        courseCreator.create()

        self.assertEqual(courseCreator.course.status, "created")

    def test_display_course(self):
        courseId = 'LDROI6775'
        expectedData = "Id cours : LDROI6775\nId professeur: 1\nDescription du cours :\n\tContenu : Introduction au droit\n\tAcquis : Code du travail\n\tMethode d'évaluation : TP et examen\nVolumes horaires :\n\tCours magistraux : 60 heures\n\tTravaux pratiques : 10 heures\n"

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
