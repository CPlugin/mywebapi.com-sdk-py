from enum import Enum

class EnChartMode(str, Enum):
    BIDPRICE = "BidPrice"
    LASTPRICE = "LastPrice"
    OLD = "Old"

    def __str__(self) -> str:
        return str(self.value)
