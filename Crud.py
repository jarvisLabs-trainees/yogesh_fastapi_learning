from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

user = []

@app.get("/")
def read():
    return user

class Model(BaseModel):
    name: str
    age:int
    address: str
    
@app.post("/post")
def create(req:Model):
    user.append(req)
    return req