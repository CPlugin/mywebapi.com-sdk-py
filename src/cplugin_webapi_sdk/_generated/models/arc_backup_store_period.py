from enum import Enum

class ArcBackupStorePeriod(str, Enum):
    MN1 = "Mn1"
    MN3 = "Mn3"
    MN6 = "Mn6"
    W1 = "W1"
    W2 = "W2"

    def __str__(self) -> str:
        return str(self.value)
