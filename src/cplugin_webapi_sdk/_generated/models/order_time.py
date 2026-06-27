from enum import Enum

class OrderTime(str, Enum):
    DAY = "Day"
    GTC = "GtC"
    SPECIFIED = "Specified"
    SPECIFIEDDAY = "SpecifiedDay"

    def __str__(self) -> str:
        return str(self.value)
