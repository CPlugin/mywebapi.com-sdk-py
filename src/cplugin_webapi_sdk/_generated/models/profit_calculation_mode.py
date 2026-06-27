from enum import Enum

class ProfitCalculationMode(str, Enum):
    CFD = "CFD"
    FOREX = "Forex"
    FUTURES = "Futures"

    def __str__(self) -> str:
        return str(self.value)
