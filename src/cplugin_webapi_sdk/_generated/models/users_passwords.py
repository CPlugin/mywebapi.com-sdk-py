from enum import Enum

class UsersPasswords(str, Enum):
    API = "API"
    INVESTOR = "Investor"
    MAIN = "Main"
    TRADER = "Trader"

    def __str__(self) -> str:
        return str(self.value)
