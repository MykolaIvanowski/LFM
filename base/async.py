import time
import asyncio


async def func1():
    task = asyncio.create_task(func2(1))
    task = asyncio.create_task(func2(2))
    task = asyncio.create_task(func2(3))

    return_value = await task
    print("A")
    await asyncio.sleep(1)
    print("B")
    print(f'returned value: {return_value}')


async def func2(n):
    print("AA"*n)
    await asyncio.sleep(1)
    n = n+1
    print("AA" * n)

asyncio.run(func1())