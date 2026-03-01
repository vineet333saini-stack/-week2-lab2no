# Starter code for FastAPI REST API assignment

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

items = {}
current_id = 0

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "description": "This is a placeholder item."}

@app.post("/items")
def create_item(item: Item):
    global current_id
    current_id += 1
    items[current_id] = item
    return {"id": current_id, **item.dict()}

# run with: uvicorn starter-code:app --reload
