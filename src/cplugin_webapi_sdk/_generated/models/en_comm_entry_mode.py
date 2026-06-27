from enum import Enum

class EnCommEntryMode(str, Enum):
    ALL = "All"
    IN = "In"
    OUT = "Out"

    def __str__(self) -> str:
        return str(self.value)
