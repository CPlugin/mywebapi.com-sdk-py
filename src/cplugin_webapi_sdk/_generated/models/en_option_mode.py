from enum import Enum

class EnOptionMode(str, Enum):
    AMERICANCALL = "AmericanCall"
    AMERICANPUT = "AmericanPut"
    EUROPEANCALL = "EuropeanCall"
    EUROPEANPUT = "EuropeanPut"

    def __str__(self) -> str:
        return str(self.value)
