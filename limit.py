from fastapi import FastAPI

limitid = FastAPI()

@limitid.get("/limit/{id}")
def limit(id: int, limit:int = 10):
    return{"id": id, "limit":limit}



