from enum import Enum

class MT5ChartRoundingRule(str, Enum):
    DOWN = "Down"
    STANDARD = "Standard"
    UP = "Up"

    def __str__(self) -> str:
        return str(self.value)
