from enum import Enum

class EnExpirationFlags(str, Enum):
    ALL = "All"
    DAY = "Day"
    GTC = "GtC"
    NONE = "None"
    SPECIFIED = "Specified"
    SPECIFIEDDAY = "SpecifiedDay"

    def __str__(self) -> str:
        return str(self.value)
