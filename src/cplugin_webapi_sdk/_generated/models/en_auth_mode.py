from enum import Enum

class EnAuthMode(str, Enum):
    RSA1024 = "Rsa1024"
    RSA2048 = "Rsa2048"
    RSACUSTOM = "RsaCustom"
    STANDARD = "Standard"

    def __str__(self) -> str:
        return str(self.value)
