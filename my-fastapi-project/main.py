# To run this API, you need to install FastAPI and Uvicorn:
# pip install "fastapi[all]" uvicorn

import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

# Create a FastAPI instance
app = FastAPI(title="Lottery Number Generator API", version="1.0.0")

# Pydantic model for the response body
class LotteryNumbers(BaseModel):
    numbers: List[int]

# Define CORS settings to allow your React front end to connect
# NOTE: In a production environment, you should replace "*" with the specific URL of your React app.
origins = ["*"]  # This allows all origins, which is good for testing.

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint for a simple health check
@app.get("/")
def read_root():
    """A simple health check endpoint."""
    return {"message": "Welcome to the Lottery Number API!"}

# Endpoint to generate lottery numbers
@app.get("/api/lottery-numbers", response_model=LotteryNumbers)
def get_lottery_numbers():
    """Generates and returns a list of 5 random numbers between 1 and 50."""
    numbers = random.sample(range(1, 51), 5)
    return {"numbers": numbers}

# To run this API locally, use the following command in your terminal:
# uvicorn main:app --reload
