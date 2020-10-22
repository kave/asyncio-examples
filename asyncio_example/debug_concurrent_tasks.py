import asyncio
import time


async def say_after(delay, msg):
    time.sleep(delay)
    print(msg)


async def run():
    task1 = asyncio.create_task(
        say_after(2, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # executes tasks concurrently
    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    asyncio.run(run(), debug=True)
