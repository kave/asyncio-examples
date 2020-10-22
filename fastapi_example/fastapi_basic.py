from typing import Optional

import uvicorn
from fastapi import FastAPI

import config

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    uvicorn.run("fastapi_basic:app", host=config.HOST, port=config.PORT, log_level="info")
