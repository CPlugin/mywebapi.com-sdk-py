from enum import Enum

class GTCMode(str, Enum):
    DAILY = "Daily"
    DAILYNOSTOPS = "DailyNoStops"
    GTC = "GTC"

    def __str__(self) -> str:
        return str(self.value)
