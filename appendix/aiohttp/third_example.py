import asyncio

async def delayed_print(text, time=1):
    await asyncio.sleep(time)
    print(text)

async def main_coro():
    task1 = asyncio.create_task(delayed_print("I'm printed second!", 2))
    task2 = asyncio.create_task(delayed_print("I'm printed first!"))


    await asyncio.gather(
        task1,
        task2,
        delayed_print("I'm printed last!", 3)
    )
    
asyncio.run(main_coro())