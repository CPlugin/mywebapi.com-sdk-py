from enum import Enum

class ClientTypes(str, Enum):
    CORPORATE = "Corporate"
    FUND = "Fund"
    INDIVIDUAL = "Individual"
    UNDEFINED = "Undefined"

    def __str__(self) -> str:
        return str(self.value)
