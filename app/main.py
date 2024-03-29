from fastapi import FastAPI

app = FastAPI()

@app.get("/")       # localhost:8000
def root():
    return {"message": "Hello Root!"}

@app.get("/home")       # localhost:8000/home
def home():
    return {"message": "Home!"}