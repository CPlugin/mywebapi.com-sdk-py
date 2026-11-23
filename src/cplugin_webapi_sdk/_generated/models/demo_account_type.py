from enum import Enum

class DemoAccountType(str, Enum):
    DISABLED = "Disabled"
    FIXED = "Fixed"
    PROLONG = "Prolong"

    def __str__(self) -> str:
        return str(self.value)
