from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")    #{item_id}에 숫자를 입력 받을 수 있음. 변수와 같음
def read_item(item_id: int, q: Union[str, None] = None):    #q에 아무것도 입력하지 않으면 Null값이 들어감
    return {"item_id": item_id, "q": q}