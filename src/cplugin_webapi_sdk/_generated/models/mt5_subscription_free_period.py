from enum import Enum

class MT5SubscriptionFreePeriod(str, Enum):
    CUSTOM = "Custom"
    DAY = "Day"
    MONTH = "Month"
    NONE = "None"
    QUARTER = "Quarter"
    WEEK = "Week"
    YEAR = "Year"

    def __str__(self) -> str:
        return str(self.value)
