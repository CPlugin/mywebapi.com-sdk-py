from enum import Enum

class MT5PluginParameterType(str, Enum):
    BOOL = "Bool"
    COLOR = "Color"
    DATE = "Date"
    DATETIME = "DateTime"
    FLOAT = "Float"
    GATEWAY = "Gateway"
    GROUPS = "Groups"
    INT = "Int"
    PERIOD = "Period"
    STRING = "String"
    SYMBOLS = "Symbols"
    TIME = "Time"
    ULTENCYMATCHINGENGINE = "UltencyMatchingEngine"
    ULTENCYPROVIDER = "UltencyProvider"
    ULTENCYSYMBOLS = "UltencySymbols"

    def __str__(self) -> str:
        return str(self.value)
