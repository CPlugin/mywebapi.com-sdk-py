from enum import Enum

class MarginLevelType(str, Enum):
    MARGINCALL = "MarginCall"
    OK = "Ok"
    STOPOUT = "StopOut"

    def __str__(self) -> str:
        return str(self.value)
