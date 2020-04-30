class Volume:

    def __init__(self, magistraux, pratique):
        #TODO raise erreur regles métiers
        self.magistraux = magistraux
        self.pratique = pratique
        self.volumes  = {"magistraux" : magistraux,
                      "pratique" : pratique}

    def getSerializedVolumes(self):
        return {"magistraux" : self.magistraux,
                "pratique" : self.pratique}



