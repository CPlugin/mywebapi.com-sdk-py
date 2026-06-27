from enum import Enum

class TickRequestFlags(str, Enum):
    ALL = "All"
    NORMAL = "Normal"
    RAW = "Raw"

    def __str__(self) -> str:
        return str(self.value)
