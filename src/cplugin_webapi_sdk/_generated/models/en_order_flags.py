from enum import Enum

class EnOrderFlags(str, Enum):
    ALL = "All"
    CLOSEBY = "CloseBy"
    LIMIT = "Limit"
    MARKET = "Market"
    NONE = "None"
    SL = "SL"
    STOP = "Stop"
    STOPLIMIT = "StopLimit"
    TP = "TP"

    def __str__(self) -> str:
        return str(self.value)
