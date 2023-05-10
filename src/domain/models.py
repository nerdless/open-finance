from enum import Enum
from typing import List, Optional
from pydantic import BaseModel


class AssetKind(str, Enum):
    land = "land"
    stock = "stock"
    debt = "debt"
    company = "company"


class AssetConfiguration(BaseModel):
    # add any additional fields that can be configured for each asset kind
    pass


class AssetBase(BaseModel):
    name: str
    default: bool = True
    currency: str
    kind: AssetKind
    industry_type: Optional[str]
    kind_configuration: Optional[AssetConfiguration]


class AssetCreate(AssetBase):
    pass


class Asset(AssetBase):
    id: int


class AccountType(str, Enum):
    cash = "cash"
    asset = "asset"


class AccountBase(BaseModel):
    include_in_net_worth: bool = True
    account_group: Optional[int]
    name: str
    type: AccountType
    assets: List[Asset] = []
    initial_balance: float = 0
    initial_date: Optional[str]
    currency: str
    icon_url: Optional[str]
    extra_fields: Optional[dict]


class AccountCreate(AccountBase):
    pass


class Account(AccountBase):
    id: int


class AccountGroupBase(BaseModel):
    name: str
    accounts: List[Account] = []


class AccountGroupCreate(AccountGroupBase):
    pass


class AccountGroup(AccountGroupBase):
    id: int


class TransactionBase(BaseModel):
    amount: float
    date: str
    origin_account_id: int
    destiny_account_id: int
    description: Optional[str]
    labels: Optional[List[str]]
    categories: Optional[List[str]]


class TransactionCreate(TransactionBase):
    pass


class Transaction(TransactionBase):
    id: int


class ExpenseBase(BaseModel):
    name: str
    currency: str
    budget: float
    withdraw_account_id: int


class ExpenseCreate(ExpenseBase):
    pass


class Expense(ExpenseBase):
    id: int


class GoalBase(BaseModel):
    name: str
    initial_cost: float
    initial_date: Optional[str]
    due_date: Optional[str]
    needed: Optional[bool] = True
    remaining_months: Optional[int]
    monthly_cost: Optional[float]


class GoalCreate(GoalBase):
    pass


class Goal(GoalBase):
    id: int