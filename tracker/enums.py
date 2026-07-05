from enum import Enum

class TypeOfCube(Enum):
    REGULAR = 1,
    MAGNETIC = 2

    @classmethod
    def choices(cls):
        return cls.name, cls.value