from src.domain.models import Value

class CurrencyConverter:
    def convert(self, value: Value, target_currency: str) -> float:
        if value.currency == target_currency:
            return value.amount
        else:
            return value.amount
