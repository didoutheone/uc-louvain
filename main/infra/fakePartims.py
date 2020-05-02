from main.common.dto.partimData import PartimData
from main.infra.config import Config
from main.infra.io import Io


class FakePartims():

    file_partims = Config().file_path_partims

    def getPartim(self):
        return Io.read(self.file_partims)

    def getPartimById(self, partimId):
        partims = self.getPartim()
        for partim in partims['partims']:
            if partim['partimId'] == partimId:
                return PartimData(partimId, partim['courseId'], partim['intitule'])

    def addPartim(self, partim):
        data = self.createData(partim)
        Io.write(self.file_partims, 'partims', data)

    def createData(self, partim):
        return {"partimId": partim.partimId, "courseId": partim.courseId, "intitule": partim.intitule}