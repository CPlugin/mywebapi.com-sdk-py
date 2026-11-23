from enum import Enum

class MT5LeverageRangeMode(str, Enum):
    VALUE = "Value"
    VALUEPERSYMBOL = "ValuePerSymbol"
    VOLUME = "Volume"
    VOLUMEPERSYMBOL = "VolumePerSymbol"

    def __str__(self) -> str:
        return str(self.value)
