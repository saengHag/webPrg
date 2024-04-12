from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
forTest = None

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

Item(forTest)


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    forTest.is_offer = q
    forTest.price = item_id
def Empty():
    if forTest == None:
        Write()
def Delete():
    forTest = None

@app.post("/items/{item_id}")
def Write(item_id: int, q: Union[str, None] = None):
    forTest.is_offer = q
    forTest.price = item_id

@app.put("/items/{item_id}")
def Update(item_id: int, q: Union[str, None] = None):
    forTest.is_offer = q
    forTest.price = item_id