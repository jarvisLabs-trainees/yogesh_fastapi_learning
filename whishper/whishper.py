import requests

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    
    API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large"
    headers = {"Authorization": "Bearer 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"}

    response = requests.post(API_URL, headers=headers, data=data)
    
    return response.json()

output = query("output.mp3")
print(output)