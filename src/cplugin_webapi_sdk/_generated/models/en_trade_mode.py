from enum import Enum

class EnTradeMode(str, Enum):
    CLOSEONLY = "CloseOnly"
    DISABLED = "Disabled"
    FULL = "Full"
    LONGONLY = "LongOnly"
    SHORTONLY = "ShortOnly"

    def __str__(self) -> str:
        return str(self.value)
