from enum import Enum

class ActivationModes(str, Enum):
    NONE = "None"
    SL = "SL"
    STOPOUT = "StopOut"
    TP = "TP"

    def __str__(self) -> str:
        return str(self.value)
