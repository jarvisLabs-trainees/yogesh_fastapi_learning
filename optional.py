from fastapi import FastAPI
from typing import Optional

option = FastAPI()

@option.get("/opion/{id}")
def index(id: int, limit:Optional[int] = 10):
    return{"id" : id, "limit" : limit}

