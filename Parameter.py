from fastapi import FastAPI


hello = FastAPI()


@hello.get("/about")
async def about():
   
    return {"About Me": "I am Yogesh"}
