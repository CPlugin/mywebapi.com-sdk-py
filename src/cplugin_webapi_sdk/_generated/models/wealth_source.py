from enum import Enum

class WealthSource(str, Enum):
    EMPLOYMENT = "Employment"
    INHERITANCE = "Inheritance"
    OTHER = "Other"
    SAVINGS = "Savings"

    def __str__(self) -> str:
        return str(self.value)
