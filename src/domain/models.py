from enum import Enum
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime
from src.tools.currency_converter import CurrencyConverter


currency_converter = CurrencyConverter()

class AssetKind(str, Enum):
    land = "land"
    stock = "stock"
    debt = "debt"
    company = "company"


class AssetConfiguration(BaseModel):
    # add any additional fields that can be configured for each asset kind
    pass


class Value(BaseModel):
    amount: float
    currency: str


class Asset(BaseModel):
    id: Optional[int]
    name: str
    value: Value
    foreign_values: List[Value]
    tags: List[str] = []
    kind: Optional[AssetKind] = None
    notes: Optional[str] = None
    industry_type: Optional[str] = None
    kind_configuration: Optional[AssetConfiguration] = None
    include_in_net_worth: Optional[bool] = False


class AccountType(str, Enum):
    cash = "cash"
    asset = "asset"
    tax = "tax"


class Account(BaseModel):
    id: Optional[int]
    name: str
    type: AccountType = AccountType.asset
    assets: List[Asset] = []
    initial_balance: float = 0
    initial_date: datetime = datetime.now()
    currency: str
    icon_url: Optional[str]
    tags: List[str] = []
    notes: Optional[str] = None
    tax_account: Optional[int] = None

    def get_current_balance(self) -> Value:
        amount = self.initial_balance + sum(
            [
                currency_converter.convert(asset.value, self.currency)
                for asset in self.assets
            ]
        )
        return Value(amount=amount, currency=self.currency)


class TransactionBase(BaseModel):
    id: Optional[int]
    name: Optional[str]
    value: Value
    foreign_values: Optional[List[Value]]
    date: datetime
    origin_account: Account
    destiny_account: Optional[Account]
    description: Optional[str]
    tags: Optional[List[str]]
    category: Optional[str]
