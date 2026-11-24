from enum import Enum

class MT5PluginMode(str, Enum):
    DISABLED = "Disabled"
    ENABLED = "Enabled"

    def __str__(self) -> str:
        return str(self.value)
