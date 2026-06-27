from enum import Enum

class EnTradeFlags(str, Enum):
    DEFAULT = "Default"
    NONE = "None"
    PROFITBYMARKET = "ProfitByMarket"
    TRADEFLAGSALL = "TradeFlagsAll"

    def __str__(self) -> str:
        return str(self.value)
