from enum import Enum

class Employment(str, Enum):
    EMPLOYED = "Employed"
    OTHER = "Other"
    RETIRED = "Retired"
    SELFEMPLOYED = "SelfEmployed"
    STUDENT = "Student"
    UNEMPLOYED = "Unemployed"

    def __str__(self) -> str:
        return str(self.value)
