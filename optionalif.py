from fastapi import FastAPI
from typing import Optional

option = FastAPI()

@option.get("/option/{id}")
async def options(id : int, limit : Optional[int] = None):
    if limit is None :
        return{"id" : id}
    else:
        return{"id" : id, "limit" : limit}
    