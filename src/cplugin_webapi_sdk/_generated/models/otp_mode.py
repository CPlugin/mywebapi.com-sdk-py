from enum import Enum

class OTPMode(str, Enum):
    DISABLED = "Disabled"
    TOTP_SHA256 = "TOTP_SHA256"

    def __str__(self) -> str:
        return str(self.value)
