from enum import Enum

class MT5SubscriptionTickHistory(str, Enum):
    ALL = "All"
    LAST2YEARS = "Last2Years"
    LAST3MONTHS = "Last3Months"
    LAST3YEARS = "Last3Years"
    LAST5YEARS = "Last5Years"
    LAST6MONTHS = "Last6Months"
    LASTDAY = "LastDay"
    LASTMONTH = "LastMonth"
    LASTWEEK = "LastWeek"
    LASTYEAR = "LastYear"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
