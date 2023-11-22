from fastapi import FastAPI
from typing import Optional 
from pydantic import BaseModel

hello = FastAPI()

@hello.get("/")
async def root():
    return{"msg" : "I am completed the first api"}
    

@hello.get("/about")
async def about():
    return{"About Me" : "I am yogesh"}

@hello.get("/user/{id}")
async def use(id : int):
    return{"id" : id}

@hello.get("/limit/{id}")
async def limit(id : int, limit : int = 10):
    return{"id" : id, "limit" : limit}

@hello.get("/limits/{id}")
def limits(id: int, limits: Optional[int] = None):
     if limits is None:
        return{"id": id}
     else:
        return{"id": id, "limits": limits}
     


class Request(BaseModel):
    name: str
    age: int

@hello.post("/")
def index(request: Request):
    return {"data": request}
