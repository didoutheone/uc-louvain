from main.model.exceptions.courseCannotBeCreated import CourseCannotBeCreated


class Volume:

    def __init__(self, magistraux, pratique):
        if not magistraux or not pratique or magistraux + pratique <= 0 :
            raise CourseCannotBeCreated
        self.magistraux = magistraux
        self.pratique = pratique
        self.volumes  = {"magistraux" : magistraux,
                      "pratique" : pratique}

    def getSerializedVolumes(self):
        return {"magistraux" : self.magistraux,
                "pratique" : self.pratique}



