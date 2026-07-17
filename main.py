from fastapi import FastAPI

from core.llm import get_llm

llm = get_llm()
response = llm.invoke("Hello, how are you?")
    
print(response)


app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Hello from Compute Engine! this is the latest updated code"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
