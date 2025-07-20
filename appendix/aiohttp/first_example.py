import asyncio

async def a_square(x):
    print(f'Asynchronously squaring {x}!')

    return x ** 2

asyncio.run(a_square(2))
