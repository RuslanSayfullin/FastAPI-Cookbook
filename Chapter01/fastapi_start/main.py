from fastapi import FastAPI

import router_example

app = FastAPI()

app.include_router(router_example.router)

@app.get("/")
def read_roor():
    return{"root": "Hello, world!"}