from enum import Enum

class EnSpliceType(str, Enum):
    ADJUSTED = "Adjusted"
    NONE = "None"
    UNADJUSTED = "Unadjusted"

    def __str__(self) -> str:
        return str(self.value)
