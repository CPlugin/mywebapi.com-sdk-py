from enum import Enum

class MT5SubscriptionControlMode(str, Enum):
    FULL = "Full"
    HIDDEN = "Hidden"
    UNSUBSCRIBE = "Unsubscribe"
    VIEW = "View"

    def __str__(self) -> str:
        return str(self.value)
