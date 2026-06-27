from enum import Enum

class MarginControllingType(str, Enum):
    CURRENCY = "Currency"
    PERCENT = "Percent"

    def __str__(self) -> str:
        return str(self.value)
