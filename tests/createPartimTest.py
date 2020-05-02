import unittest

from main.exposition.displayPartim import DisplayPartim
from main.exposition.partimCreationRequest import PartimCreationRequest
from main.infra.fakePartims import FakePartims
from main.use_case.createPartim import CreatePartim


class CreatePartimTest(unittest.TestCase):

    def test_create_partim(self):
        profilId = 1
        courseId = "LDROI6775"
        intitule = "Premiere partie du cours"
        request = PartimCreationRequest(profilId, courseId, intitule)
        partimCreator = CreatePartim(request, FakePartims())
        partimCreator.create()

        self.assertEqual(partimCreator.partim.status, "created")

    def test_display_partim(self):
        partimId = "LDROI6775A"
        expectedData = "Id partim : LDROI6775A\nId cours associé: LDROI6775\nIntitulé : Premiere partie du cours\n"

        actualData = DisplayPartim(partimId).displayPartim()

        self.assertEqual(actualData, expectedData)


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
