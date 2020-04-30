from main.courseGen.use_case.iFacultyRepository import IFacultyRepository


class FacultyRepository:
    def getFaculties(self):
        return IFacultyRepository.getFalculties()