from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from typing import List
import requests

app = FastAPI()

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    
    API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large"
    headers = {"Authorization": "Bearer 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"}

    response = requests.post(API_URL, headers=headers, data=data)
    
    return response.json()

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        output = query(file.filename)
        return JSONResponse(content=output)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
