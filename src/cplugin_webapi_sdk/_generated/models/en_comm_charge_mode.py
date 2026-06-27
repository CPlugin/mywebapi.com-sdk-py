from enum import Enum

class EnCommChargeMode(str, Enum):
    DAILY = "Daily"
    INSTANT = "Instant"
    MONTHLY = "Monthly"

    def __str__(self) -> str:
        return str(self.value)
