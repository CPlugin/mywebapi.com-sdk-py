from enum import Enum

class MarginCalculationMode(str, Enum):
    CFD = "CFD"
    CFDINDEX = "CFDIndex"
    CFDLEVERAGE = "CFDLeverage"
    FOREX = "Forex"
    FUTURES = "Futures"

    def __str__(self) -> str:
        return str(self.value)
