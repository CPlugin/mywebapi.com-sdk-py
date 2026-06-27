from enum import Enum

class DataFeedMode(str, Enum):
    NEWS = "News"
    QUOTES = "Quotes"
    QUOTESNEWS = "QuotesNews"

    def __str__(self) -> str:
        return str(self.value)
