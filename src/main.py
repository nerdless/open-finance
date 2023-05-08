from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Expense(BaseModel):
    id: int
    description: str
    amount: float

expenses = []

@app.get("/expenses")
async def get_expenses():
    return expenses

@app.post("/expenses")
async def add_expense(expense: Expense):
    expenses.append(expense)
    return expense