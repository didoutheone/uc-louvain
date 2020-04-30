class Description:
    def __init__(self,contenu, acquis, methode_evaluation):
        #TODO raise erreur regles métiers
        self.contenu = contenu
        self.acquis = acquis
        self.methode_evaluation = methode_evaluation
        self.descriptions =  {"contenu" : contenu,
                             "acquis": acquis,
                              "methode_evaluation": methode_evaluation}

    def getSerializedDescriptions(self):
        return {"contenu" : self.contenu,
                "acquis": self.acquis,
                "methode_evaluation": self.methode_evaluation}