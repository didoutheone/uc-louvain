import unittest

from main.courseGen.exposition.displayCourse import DisplayCourse
from main.courseGen.exposition.generatorRequest import GeneratorRequest
from main.courseGen.model.description import Description
from main.courseGen.model.volume import Volume
from main.courseGen.use_case.generateCourse import GenerateCourse
from main.infra.fakeCourses import FakeCourses


class GenerateCourseTest(unittest.TestCase):

    def test_generate_course(self):
        profilId = 1
        descriptions = Description("du droit", "test2", "gros exam")
        volumes = Volume(20, 5)
        request = GeneratorRequest(profilId, descriptions, volumes)

        generator = GenerateCourse(request, FakeCourses())
        generator.generate()

        self.assertEqual(generator.course.status, "created")

    def test_display_course(self):
        courseId = 'LDROI1623'
        expectedData = "Id cours : LDROI1623\nId professeur: 1\nDescription du cours :\n\tContenu : du droit\n\tAcquis : plus de droit\n\tMethode d'évaluation : gros exam\nVolumes horaires :\n\tCours magistraux : 20 heures\n\tTravaux pratiques : 5 heures\n"

        actual = DisplayCourse(courseId).displayCourse()

        self.assertEqual(actual, expectedData)