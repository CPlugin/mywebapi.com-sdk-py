from enum import Enum

class TradingExperience(str, Enum):
    ABOVETHREEYEARS = "AboveThreeYears"
    LESSTHANYEAR = "LessThanYear"
    ONETOTHREEYEARS = "OneToThreeYears"

    def __str__(self) -> str:
        return str(self.value)
