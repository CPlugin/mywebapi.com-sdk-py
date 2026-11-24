from enum import Enum

class MT5SubscriptionStatus(str, Enum):
    ACTIVE = "Active"
    CANCELED = "Canceled"
    SUSPENDED = "Suspended"

    def __str__(self) -> str:
        return str(self.value)
