import time
import asyncio
from fastapi import FastAPI

app = FastAPI()

@app.get("/sync")
def read_sync():
    time.sleep(2)
    return {
        "message": "Synchrounouns blocling endpoint"
    }

@app.get("/async")
async def read_async():
    await asyncio.sleep(2)
    return {
        "message": "Asynchromous non-blocking endpoint"
    }

