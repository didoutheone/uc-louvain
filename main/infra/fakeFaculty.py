from main.use_case.faculties import Faculties


class FakeFaculty:
    def getFaculties(self):
        return Faculties.getFalculties()