from enum import Enum

class WatchdogState(str, Enum):
    DISCONNECTED = "Disconnected"
    SYNCHRONIZED = "Synchronized"
    SYNCHRONIZING = "Synchronizing"

    def __str__(self) -> str:
        return str(self.value)
