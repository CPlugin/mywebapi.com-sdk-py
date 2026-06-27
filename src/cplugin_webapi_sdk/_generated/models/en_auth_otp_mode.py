from enum import Enum

class EnAuthOTPMode(str, Enum):
    DISABLED = "Disabled"
    TOTPSHA256 = "TotpSha256"
    TOTPSHA256WEB = "TotpSha256Web"

    def __str__(self) -> str:
        return str(self.value)
