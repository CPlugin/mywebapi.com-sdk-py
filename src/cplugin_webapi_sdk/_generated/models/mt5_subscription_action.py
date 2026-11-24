from enum import Enum

class MT5SubscriptionAction(str, Enum):
    CANCEL = "Cancel"
    DELETED = "Deleted"
    RENEWAL = "Renewal"
    SUBSCRIBE = "Subscribe"
    SUSPEND = "Suspend"

    def __str__(self) -> str:
        return str(self.value)
