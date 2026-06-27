from enum import Enum

class ExportExecutionPeriod(str, Enum):
    H1 = "H1"
    M1 = "M1"
    M15 = "M15"
    M30 = "M30"
    M5 = "M5"

    def __str__(self) -> str:
        return str(self.value)
