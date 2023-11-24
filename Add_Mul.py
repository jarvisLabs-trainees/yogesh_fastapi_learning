from fastapi import FastAPI

add = FastAPI()
@add.get("/add")
def mul(x: int , y:int, z:int):
    value = (x + y)*z
    return{"Value" : value}