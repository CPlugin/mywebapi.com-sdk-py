from enum import Enum

class MarginMode(str, Enum):
    DONTUSE = "DontUse"
    USEALL = "UseAll"
    USELOSS = "UseLoss"
    USEPROFIT = "UseProfit"

    def __str__(self) -> str:
        return str(self.value)
