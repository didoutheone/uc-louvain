from main.infra.fakePartims import FakePartims


class DisplayPartim():
    def __init__(self, partimId):
        self.partimId = partimId

    def displayPartim(self):
        partim = FakePartims().getPartimById(self.partimId)
        data = self.displayData(partim)
        return data

    def displayData(self, partimData):
        return "Id partim : " + partimData.partimId + "\nId cours associé: " + str(partimData.courseId) + "\nIntitulé : " + str(partimData.intitule) + "\n"