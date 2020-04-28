import random
import string


class IdUtils:
    def create_unique_id(self):
        id = ("".join(random.choice(string.digits) for _ in range(4)))
        print("LDROI" + id)