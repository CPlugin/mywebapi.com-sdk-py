from enum import Enum

class RolloverMode(str, Enum):
    NORMAL = "Normal"
    REOPENBYBID = "ReopenByBid"
    REOPENBYCLOSEPRICE = "ReopenByClosePrice"

    def __str__(self) -> str:
        return str(self.value)
