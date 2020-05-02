import abc

class Partims:

    @abc.abstractmethod
    def getPartims(self):
        pass

    @abc.abstractmethod
    def addPartim(self, course):
        pass

    @abc.abstractmethod
    def getPartimById(self, partimId):
        pass