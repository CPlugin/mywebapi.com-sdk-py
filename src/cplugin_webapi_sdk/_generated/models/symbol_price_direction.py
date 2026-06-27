from enum import Enum

class SymbolPriceDirection(str, Enum):
    DOWN = "Down"
    NONE = "None"
    UP = "Up"

    def __str__(self) -> str:
        return str(self.value)
