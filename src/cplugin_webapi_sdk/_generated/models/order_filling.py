from enum import Enum

class OrderFilling(str, Enum):
    BOC = "BoC"
    FOK = "FoK"
    IOC = "IoC"
    RETURN = "Return"

    def __str__(self) -> str:
        return str(self.value)
