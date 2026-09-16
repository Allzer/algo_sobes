import asyncio
import time


async def task(name, delay):
    print(f'{name} started')
    await asyncio.sleep(delay=delay)
    print(f'{name} finished')

async def main():
    start = time.time()
    await asyncio.gather(
        task("A", 2),
        task("B", 1),
        task("C", 3),
        task("D", 3),
    )

    # await task("qwe", 1)

    print(time.time() - start)
    print("all task complete")

asyncio.run(main())