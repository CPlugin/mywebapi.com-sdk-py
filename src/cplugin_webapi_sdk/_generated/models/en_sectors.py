from enum import Enum

class EnSectors(str, Enum):
    BASICMATERIALS = "BasicMaterials"
    COMMODITIES = "Commodities"
    COMMUNICATIONSERVICES = "CommunicationServices"
    CONSUMERCYCLICAL = "ConsumerCyclical"
    CONSUMERDEFENSIVE = "ConsumerDefensive"
    CURRENCY = "Currency"
    CURRENCYCRYPTO = "CurrencyCrypto"
    ENERGY = "Energy"
    FINANCIAL = "Financial"
    HEALTHCARE = "Healthcare"
    INDEXES = "Indexes"
    INDUSTRIALS = "Industrials"
    REALESTATE = "RealEstate"
    TECHNOLOGY = "Technology"
    UNDEFINED = "Undefined"
    UTILITIES = "Utilities"

    def __str__(self) -> str:
        return str(self.value)
