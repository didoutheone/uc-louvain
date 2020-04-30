import random
import string


class IdGenerator():

    def create_unique_id(self, faculty):
        id = (faculty + "DROI") + str(random.randint(1000, 9999))
        return id