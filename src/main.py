from fastapi import FastAPI
from src.domain.models import Asset, AssetCreate, Account, AccountCreate
from typing import List

app = FastAPI()


@app.post("/assets/", response_model=Asset)
def create_asset(asset: AssetCreate):
    return {"id": 1, **asset.dict()}

@app.get("/assets/{asset_id}", response_model=Asset)
def read_asset(asset_id: int):
    return {"id": asset_id, "name": "Test Asset", "default": True}

@app.post("/accounts/", response_model=Account)
def create_account(account: AccountCreate):
    return {"id": 1, **account.dict()}

@app.get("/accounts/{account_id}", response_model=Account)
def read_account(account_id: int):
    return {"id": account_id, "name": "Test Account", "type": "cash", "assets": []}