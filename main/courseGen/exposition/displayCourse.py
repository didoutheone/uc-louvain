from main.courseGen.use_case.iCourseRepository import ICourseRepository


class DisplayCourse():
    def __init__(self, courseId):
        self.courseId = courseId

    def displayCourse(self):
        course = ICourseRepository().getCourseById(self.courseId)
        data = self.displayData(course)
        return data

    def displayData(self, courseData):
        return "Id cours : " + courseData.courseId + "\nId professeur: " + str(courseData.profilId) + "\nDescription du cours :\n\tContenu : " + courseData.descriptions['contenu'] + "\n\tAcquis : " + courseData.descriptions['acquis'] + "\n\tMethode d'évaluation : " + courseData.descriptions['methode_evaluation'] + "\nVolumes horaires :\n\tCours magistraux : " + str(courseData.volumes['magistraux']) + " heures\n\tTravaux pratiques : " + str(courseData.volumes['pratique']) + " heures\n"