from fastapi import FastAPI
import requests  
hello = FastAPI() 

@hello.get("/use")
async def World():  
    response = requests.get("https://251a8a844dfb0ccb53da1c450e008d30.notebooksb.jarvislabs.net/use")
    return response.json();
