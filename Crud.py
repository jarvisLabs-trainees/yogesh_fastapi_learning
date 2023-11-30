from fastapi import FastAPI,Path,Query
from pydantic import BaseModel
from typing import Optional


app = FastAPI()

#storing the user details
user = []

class Model(BaseModel):
    name: str
    age:int
    address: str
#read the user detailss
@app.get("/User")
def read():
    return user

#post the user details
@app.post("/User")
def create(req:Model):
    user.append(req)
    return req

#We give the id and its give the id details 
@app.get("/User/{id}")
#29th line id we want to use interger and use path also 
def get_user(id:int=Path(...,description="The Id of the user you want to retrived.",gt=2),AddNewData:str = Query(None,max_length=5) ): 
    return {"Userid": user[id],"Query":AddNewData}