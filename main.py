from fastapi import FastAPI
import random

app = FastAPI()

first_names = [
    "John",
    "Doe",
    "Jack",
    "Davis",
    "Steve",
    "Alan",
    "Tom",
    "Chris",
    "Joe",
    "Richard"
]

last_names = [
    "Brown",
    "Miller",
    "McKalie",
    "Winder",
    "West",
    "Prat",
    "Hanks",
    "Evan",
    "Grake",
    "William"
]

@app.get("/")
async def root():
    first_name, last_name = random.choice(first_names), random.choice(last_names)
    return {
        "name": first_name + " " + last_name,
        "first_name": first_name,
        "last_name": last_name,
        "age": random.randint(15, 60),
        "email": first_name.lower() + last_name.lower() + "@gmail.com",
    }
