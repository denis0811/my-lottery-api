from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

# Temporarily allow all origins for debugging purposes.
# WARNING: This is not recommended for production environments.
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/lottery-numbers")
def get_lottery_numbers():
    # Simulated pool of frequently drawn EuroMillions numbers (based on historical data)
    frequent_main_numbers = [4, 19, 23, 25, 27, 28, 29, 31, 34, 38, 42, 44, 46, 48, 50]
    frequent_lucky_stars = [2, 3, 5, 8, 9, 11]

    # Randomly select 5 unique main numbers from the pool
    main_numbers = random.sample(frequent_main_numbers, 5)

    # Randomly select 2 unique Lucky Star numbers from the pool
    lucky_stars = random.sample(frequent_lucky_stars, 2)

    # Sort for neatness
    main_numbers.sort()
    lucky_stars.sort()
    
    # Return a dictionary with both number sets, which FastAPI will automatically convert to JSON.
    return {"main_numbers": main_numbers, "lucky_stars": lucky_stars}
