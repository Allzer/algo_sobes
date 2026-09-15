import asyncio
import time

def task(name):
    print(f'start task {name}')
    time.sleep(2)
    print(f'finish task {name}')

def main():
    task('A')
    task('B')
    task('C')

start = time.time()
main()
print('sync time: ', time.time()-start)



async def task_async(name):
    print(f'start async task {name}')
    await asyncio.sleep(2)
    print(f'finish async task {name}')

async def async_main():
    await asyncio.gather( #gather - даёт возможность запустить корутины конкурентно и дождаться завершения их всех
        task_async('A'),
        task_async('B'),
        task_async('C'),
    )

start = time.time()
asyncio.run(async_main())
print('async time: ', time.time()-start)
