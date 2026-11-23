from enum import Enum

class ClientOrigins(str, Enum):
    CONTEST = "Contest"
    DEMO = "Demo"
    MANUAL = "Manual"
    PRELIMINARY = "Preliminary"
    REAL = "Real"

    def __str__(self) -> str:
        return str(self.value)
