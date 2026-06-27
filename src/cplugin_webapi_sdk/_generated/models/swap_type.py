from enum import Enum

class SwapType(str, Enum):
    DOLLARS = "Dollars"
    INTEREST = "Interest"
    MARGINCURRENCY = "MarginCurrency"
    POINTS = "Points"

    def __str__(self) -> str:
        return str(self.value)
