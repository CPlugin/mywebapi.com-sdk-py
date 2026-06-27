from enum import Enum

class TradeModifyFlags(str, Enum):
    ADMIN = "Admin"
    ALL = "All"
    APIADMIN = "ApiAdmin"
    APIGATEWAY = "ApiGateway"
    APIMANAGER = "ApiManager"
    APISERVER = "ApiServer"
    MANAGER = "Manager"
    NONE = "None"
    POSITION = "Position"
    RESTORE = "Restore"

    def __str__(self) -> str:
        return str(self.value)
