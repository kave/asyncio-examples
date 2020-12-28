import asyncio
import time


async def say_after(delay, msg):
    await asyncio.sleep(delay)  # non-blocking action
    print(msg)


async def run():
    print(f"started at {time.strftime('%X')}")

    # pauses application execution for each coroutine
    # allows the event loop to handle other requests during the pause

    await say_after(2, 'hello')
    await say_after(2, 'world')

    # should take 4 seconds to complete
    print(f"finished at {time.strftime('%X')}")


if __name__ == '__main__':
    # print(run())
    asyncio.run(run(), debug=True)
