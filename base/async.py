import asyncio


async def main_func():
    task = asyncio.create_task(func_task(1))
    task = asyncio.create_task(func_task(2))
    task = asyncio.create_task(func_task(3))

    return_value = await task
    print("A")
    await asyncio.sleep(1)
    print("B")
    print(f'returned value: {return_value}')


async def func_task(n):
    print("AA"*n)
    await asyncio.sleep(1)
    n = n+1
    print("AA" * n)

asyncio.run(main_func())


# example 2
print("******* example 2 ********")


# this works synchronous (incorrect)
async def main_job():
    for task in (1,1,3,2):
        await synk_task(task)


# this works correctly asynchronous
async def main_job():
    coroutine = [synk_task(task=task) for task in ( 1,1,3,2)]
    await asyncio.gather(*coroutine)


async def synk_task(task):
    print("task  starts: ",task)
    await asyncio.sleep(task)
    print("task finished: ",task)


asyncio.run(main_job())
