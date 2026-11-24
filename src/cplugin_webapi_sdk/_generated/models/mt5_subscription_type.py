from enum import Enum

class MT5SubscriptionType(str, Enum):
    FOLDER = "Folder"
    SUBSCRIPTION = "Subscription"

    def __str__(self) -> str:
        return str(self.value)
