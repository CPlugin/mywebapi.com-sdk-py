from enum import Enum

class EnGtcMode(str, Enum):
    DAILY = "Daily"
    DAILYNOSTOPS = "DailyNoStops"
    GTC = "GtC"

    def __str__(self) -> str:
        return str(self.value)
