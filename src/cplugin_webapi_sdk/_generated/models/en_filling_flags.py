from enum import Enum

class EnFillingFlags(str, Enum):
    ALL = "All"
    BOC = "BoC"
    FOK = "FoK"
    IOC = "IoC"
    NONE = "None"

    def __str__(self) -> str:
        return str(self.value)
