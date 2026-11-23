from enum import Enum

class EducationLevel(str, Enum):
    BACHELOR = "Bachelor"
    HIGHSCHOOL = "HighSchool"
    MASTER = "Master"
    NONE = "None"
    OTHER = "Other"
    PHD = "PHD"

    def __str__(self) -> str:
        return str(self.value)
