import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import requests
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all domains (for testing)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# URL of Account Service
ACCOUNT_SERVICE_URL = os.getenv("ACCOUNT_SERVICE_URL", "http://localhost:8080")

# Request model


class BuySellRequest(BaseModel):
    id: int
    amount: int


@app.post("/buy")
async def buy_cryptos(request: BuySellRequest):
    """Handles buying tbzCoins for a user"""
    if request.amount <= 0:
        raise HTTPException(
            status_code=400, detail="Amount must be greater than 0")

    try:
        response = requests.post(
            f"{ACCOUNT_SERVICE_URL}/Account/AddCrypto",
            params={"userId": request.id, "amount": request.amount},
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=500, detail=f"Fehler bei der Backend-Anfrage: {str(e)}"
        )

    return {"success": response.status_code == 200}


@app.post("/sell")
async def sell_cryptos(request: BuySellRequest):
    """Handles selling tbzCoins"""
    if request.amount <= 0:
        raise HTTPException(
            status_code=400, detail="Amount must be greater than 0")

    try:
        balance_response = requests.post(
            f"{ACCOUNT_SERVICE_URL}/Account/RemoveCrypto",
            params={"userId": request.id, "amount": request.amount},
        )
        balance_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=500, detail=f"Fehler beim Abrufen des Guthabens: {str(e)}"
        )
