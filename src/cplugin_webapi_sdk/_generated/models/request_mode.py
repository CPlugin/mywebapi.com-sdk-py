from enum import Enum

class RequestMode(str, Enum):
    RANGEIN = "RangeIn"
    RANGEINEXCLUDEOUTOFRAGE = "RangeInExcludeOutOfRage"
    RANGELAST = "RangeLast"
    RANGEOUT = "RangeOut"

    def __str__(self) -> str:
        return str(self.value)
