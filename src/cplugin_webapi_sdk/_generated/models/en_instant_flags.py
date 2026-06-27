from enum import Enum

class EnInstantFlags(str, Enum):
    ALL = "All"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
