from enum import Enum

class EnMarginCalcFlags(str, Enum):
    CLEARACC = "ClearAcc"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
