from enum import Enum

class EntryFlag(str, Enum):
    IN = "In"
    INOUT = "InOut"
    OUT = "Out"
    OUTBY = "OutBy"

    def __str__(self) -> str:
        return str(self.value)
