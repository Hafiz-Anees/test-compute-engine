from fastapi import FastAPI

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
