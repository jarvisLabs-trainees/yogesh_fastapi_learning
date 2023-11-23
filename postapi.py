from fastapi import FastAPI
from pydantic import BaseModel
import requests


add = FastAPI()

class Request(BaseModel):
    num1:int
    num2:int

@add.post("/sums")
async def index(data : Request):
    Responces = requests.post("https://251a8a844dfb0ccb53da1c450e008d30.notebooksb.jarvislabs.net/sum",data=data.json())
    return Responces.json()
    