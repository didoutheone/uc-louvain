from main.common.events import mailEvent
from main.common.events.event import Event
from main.infra.fakeTeachers import FakeTeachers
from main.model.partim import Partim


class CreatePartim:

    def __init__(self, request, repository):
        self.request = request
        self.partim = None
        self.partimData = None
        self.partimRepository = repository

    def create(self):
        teacherData = FakeTeachers().findTeacherById(self.request.profilId)
        self.partim = Partim(self.request, teacherData)
        self.partim = self.partim.createPartim()
        self.partimData = self.partim.getPartimData()
        self.partimRepository.addPartim(self.partimData)
        # if self.partim.status == "created":
        #     event = Event()
        #     event += mailEvent.mailEvent
        #     event.notify(self.partim.teacher.profilId, self.partim.courseId, self.partim.teacher.faculty)