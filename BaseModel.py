from fastapi import FastAPI
from pydantic import BaseModel

base = FastAPI()

class Request(BaseModel):
    name : str
    age : int

@base.post("/")
def index(request: Request):
        return{"request" : request}
