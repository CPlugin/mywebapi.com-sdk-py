from enum import Enum

class EnSwapFlags(str, Enum):
    CONSIDERHOLIDAYS = "ConsiderHolidays"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
