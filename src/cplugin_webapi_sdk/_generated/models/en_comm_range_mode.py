from enum import Enum

class EnCommRangeMode(str, Enum):
    OVERTURNMONEY = "OverturnMoney"
    OVERTURNVOLUME = "OverturnVolume"
    PROFIT = "Profit"
    VALUE = "Value"
    VOLUME = "Volume"

    def __str__(self) -> str:
        return str(self.value)
