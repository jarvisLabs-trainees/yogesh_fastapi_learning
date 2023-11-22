from fastapi import FastAPI

userid = FastAPI()

@userid.get("/user/{id}")
def user(id: int):
    return{"id" : id}