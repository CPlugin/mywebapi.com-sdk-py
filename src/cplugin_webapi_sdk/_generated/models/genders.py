from enum import Enum

class Genders(str, Enum):
    FEMALE = "Female"
    MALE = "Male"
    UNSPECIFIED = "Unspecified"

    def __str__(self) -> str:
        return str(self.value)
