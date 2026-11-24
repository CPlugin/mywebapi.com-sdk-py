from enum import Enum

class MT5SubscriptionSymbolLevel(str, Enum):
    DELAYED = "Delayed"
    REALTIMELEVEL1 = "RealtimeLevel1"
    REALTIMELEVEL2 = "RealtimeLevel2"

    def __str__(self) -> str:
        return str(self.value)
