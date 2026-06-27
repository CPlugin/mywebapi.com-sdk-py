from enum import Enum

class EnInstantMode(str, Enum):
    NORMAL = "Normal"

    def __str__(self) -> str:
        return str(self.value)
