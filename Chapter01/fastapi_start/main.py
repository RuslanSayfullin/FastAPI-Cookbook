from fastapi import FastAPI

from router_example import router

app = FastAPI()

app.include_router(router)

@app.get("/")
async def read_root():
    return {"Hello": "Wor;d"}