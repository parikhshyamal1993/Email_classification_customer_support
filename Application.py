from source.email_classification import predict
from typing import Annotated , Union
from fastapi import FastAPI, Header , Form , Body
from pydantic import BaseModel
from config.params import attibute_list
import uvicorn


app = FastAPI()


class Item(BaseModel):
    text: str
    
class Transaction_Headers(BaseModel):
    user: str
    password:str
    Correlation_id: str

@app.post("/email_classification")
def read_root(
    correlation_id: Annotated[str, Header()],
    text: Annotated[str, Form()],
    token: Annotated[str, Form()],):
    
    probas_list , id , name = predict(text)
    return {
        "correlation_id": correlation_id,
        "classification":name}

@app.get("/health")
def health():
    return {"health":"True"}


def start_server():
    # print('Starting Server...')       

    uvicorn.run(
        "Application:app",
        host="0.0.0.0",
        port=int(attibute_list['port']),
        log_level="debug",
    )


if __name__ == "__main__":
    start_server()

