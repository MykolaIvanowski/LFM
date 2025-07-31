import threading
import queue
import time

q = queue.Queue()

def producer():
    for i in range(5):
        print(f"Producing {i}")
        q.put(i)
        time.sleep(1)

def consumer():
    while True:
        item = q.get()
        print(f"Consuming {item}")
        q.task_done()

threading.Thread(target=producer).start()
threading.Thread(target=consumer, daemon=True).start()

q.join()


######################

import asyncio

async def producer(q):
    for i in range(5):
        print(f"Producing {i}")
        await q.put(i)
        await asyncio.sleep(1)

async def consumer(q):
    while True:
        item = await q.get()
        print(f"Consuming {item}")
        q.task_done()

async def main():
    q = asyncio.Queue()
    await asyncio.gather(producer(q), consumer(q))

asyncio.run(main())