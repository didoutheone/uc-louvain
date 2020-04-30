from main.infra.dbUtils import DbUtils


class CourseData:
    def __init__(self, id, faculty, teachers, descriptions, volumes):
        self.id = id
        self.faculty = faculty
        self.teachers = teachers
        self.descriptions = descriptions
        self.volumes = volumes
        self.file = " home/clementine/Documents/Soat/formation_ddd/uc-louvain/db/teachers.json"
