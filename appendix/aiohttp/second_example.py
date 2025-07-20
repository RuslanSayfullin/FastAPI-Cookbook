import asyncio

async def sleeper(x):
    await asyncio.sleep(x)
    return x + 1

async def waiter(x):
    sleepy_result = (await sleeper(x)) ** 2
    return sleepy_result

asyncio.run(waiter(2))