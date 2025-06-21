from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    #  http://127.0.0.1:8000/items/42?q=example
    return {"item_id": item_id, "query": q}