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
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# URL of Account Service
ACCOUNT_SERVICE_URL = os.getenv("ACCOUNT_SERVICE_URL", "http://localhost:8080")


class SendRequest(BaseModel):
    id: int
    receiverId: int
    amount: int


@app.post("/send")
async def send_cryptos(request: SendRequest):
    """Handles sending tbzCoins to a friend."""

    if request.amount <= 0:
        raise HTTPException(
            status_code=400, detail="Amount must be greater than 0")

    # ✅ Step 1: Check if receiver is a friend
    try:
        friends_response = requests.get(
            f"{ACCOUNT_SERVICE_URL}/Account/Friends",
            params={"userId": request.id},  # ✅ Use query params
        )
        friends_response.raise_for_status()
        friends = friends_response.json()

        # ✅ Debug: Print response
        print("Friends List Response:", friends_response.text)
    except requests.exceptions.RequestException as e:
        print("Error fetching friend list:", e)
        raise HTTPException(
            status_code=500, detail="Error fetching friend list")

    if not any(friend["id"] == request.receiverId for friend in friends):
        raise HTTPException(status_code=403, detail="Receiver is not a friend")

    # ✅ Step 2: Check Sender's Balance (Handle raw number response)
    try:
        balance_response = requests.get(
            f"{ACCOUNT_SERVICE_URL}/Account/Cryptos",
            params={"userId": request.id},  # ✅ Use query params
        )
        balance_response.raise_for_status()

        # ✅ Fix: Convert raw number response to int
        sender_balance = int(balance_response.text.strip())

        # ✅ Debug: Print balance
        print(f"Sender's Balance: {sender_balance}")
    except (requests.exceptions.RequestException, ValueError) as e:
        print("Error fetching sender balance:", e)
        raise HTTPException(
            status_code=500, detail="Error fetching sender balance")

    if sender_balance < request.amount:
        raise HTTPException(status_code=400, detail="Insufficient balance")

    # ✅ Step 3: Transfer tbzCoins (Deduct from sender, Add to receiver)
    try:
        # ✅ Deduct from sender
        sender_update = requests.post(
            f"{ACCOUNT_SERVICE_URL}/Account/RemoveCrypto",
            # ✅ Use query params
            params={"userId": request.id, "amount": request.amount},
        )
        sender_update.raise_for_status()

        # ✅ Debug: Print response
        print("Sender Update Response:", sender_update.text)

        # ✅ Add to receiver
        receiver_update = requests.post(
            f"{ACCOUNT_SERVICE_URL}/Account/AddCrypto",
            params={"userId": request.receiverId,
                    "amount": request.amount},  # ✅ Use query params
        )
        receiver_update.raise_for_status()

        # ✅ Debug: Print response
        print("Receiver Update Response:", receiver_update.text)

    except requests.exceptions.RequestException as e:
        print("Error updating balances:", e)
        raise HTTPException(status_code=500, detail="Error updating balances")

    return {"message": "Transaction successful"}  # ✅ Proper response
