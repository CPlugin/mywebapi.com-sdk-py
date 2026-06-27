from enum import Enum

class EnReportsMode(str, Enum):
    DISABLED = "Disabled"
    EODONLY = "EODOnly"
    EOMONLY = "EOMOnly"
    FULL = "Full"

    def __str__(self) -> str:
        return str(self.value)
