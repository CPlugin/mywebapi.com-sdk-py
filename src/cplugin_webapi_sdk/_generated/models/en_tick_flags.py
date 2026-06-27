from enum import Enum

class EnTickFlags(str, Enum):
    ALL = "All"
    COLLECTRAW = "CollectRaw"
    FEEDSTATS = "FeedStats"
    NEGATIVEPRICES = "NegativePrices"
    NONE = "None"
    REALTIME = "Realtime"

    def __str__(self) -> str:
        return str(self.value)
