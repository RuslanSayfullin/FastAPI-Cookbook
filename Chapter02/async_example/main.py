import time
import asyncio

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/sync")
def read_sync():
    time.sleep(2)
    return {
        "Message": "Synchrounouns blocking endpoint"
    }

@app.get("/async")
async def read_async():
    await asyncio.sleep(2)
    return {"Message": "Asynchronous non-blocking endpoint"}

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)