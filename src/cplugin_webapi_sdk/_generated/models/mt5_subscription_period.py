from enum import Enum

class MT5SubscriptionPeriod(str, Enum):
    ANNUAL = "Annual"
    CUSTOM = "Custom"
    DAILY = "Daily"
    MONTHLY = "Monthly"
    ONCE = "Once"
    QUARTERLY = "Quarterly"
    WEEKLY = "Weekly"

    def __str__(self) -> str:
        return str(self.value)
