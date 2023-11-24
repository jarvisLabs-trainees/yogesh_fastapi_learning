from fastapi import FastAPI

add = FastAPI()
@add.get("/sum")
def cal():
    return {"Addation" : 2+2}
