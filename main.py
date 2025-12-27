import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return jsonify({"message": "hello world"})
