from fastapi import FastAPI

import requests

app = FastAPI()

@app.get("/")
def root():
    URL = "https://bigdata.kepco.co.kr/openapi/v1/powerUsage/industryType.do?year=2020&month=11&metroCD=11&cityCd=12&apiKey=s0VBUy1c7ma5Gcp6E3Pyg0i0Kj7KMkmhUv7KORAy&returnType=json"
    
    contents = requests.get(URL).text

    return { "message": contents }

@app.get("/home")
def home():
    return { "message": "Home!" }