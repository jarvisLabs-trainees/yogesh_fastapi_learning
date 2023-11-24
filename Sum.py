from fastapi import FastAPI
from typing import Optional


mul = FastAPI()
@mul.get("/adding")
def add(x:int, y: int, z:Optional[int]= None):
    if z is  None :
        return{"Adding two number":x + y}
    else :
        return{"Adding three number": x + y + z}