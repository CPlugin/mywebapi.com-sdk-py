from enum import Enum

class EnDealAction(str, Enum):
    AGENT = "Agent"
    AGENTDAILY = "AgentDaily"
    AGENTMONTHLY = "AgentMonthly"
    BALANCE = "Balance"
    BONUS = "Bonus"
    BUY = "Buy"
    BUYCANCELED = "BuyCanceled"
    CHARGE = "Charge"
    COMMISSION = "Commission"
    COMMISSIONDAILY = "CommissionDaily"
    COMMISSIONMONTHLY = "CommissionMonthly"
    CORRECTION = "Correction"
    CREDIT = "Credit"
    DIVIDEND = "Dividend"
    DIVIDENDFRANKED = "DividendFranked"
    INTERESTRATE = "InterestRate"
    SELL = "Sell"
    SELLCANCELED = "SellCanceled"
    SOCOMPENSATION = "SOCompensation"
    TAX = "Tax"

    def __str__(self) -> str:
        return str(self.value)
