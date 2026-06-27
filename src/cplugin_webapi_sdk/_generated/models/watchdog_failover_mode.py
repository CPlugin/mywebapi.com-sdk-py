from enum import Enum

class WatchdogFailoverMode(str, Enum):
    FULL = "Full"
    MOST = "Most"
    OFF = "Off"

    def __str__(self) -> str:
        return str(self.value)
