from enum import Enum

class SoActivation(str, Enum):
    MARGINCALL = "MarginCall"
    NONE = "None"
    STOPOUT = "StopOut"

    def __str__(self) -> str:
        return str(self.value)
