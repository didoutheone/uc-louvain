class CourseCreationRequest:
    def __init__(self, profilId, descriptions, volumes):
        self.profilId = profilId
        self.courseId = None
        self.descriptions = descriptions
        self.volumes = volumes
