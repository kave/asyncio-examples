import asyncio
import time

""" https://docs.python.org/3/library/asyncio-dev.html
asyncio checks for coroutines that were not awaited and logs them; this mitigates the “forgotten await” pitfall.

Many non-threadsafe asyncio APIs (such as loop.call_soon() and loop.call_at() methods) raise an exception if they are called from a wrong thread.

The execution time of the I/O selector is logged if it takes too long to perform an I/O operation.

Callbacks taking longer than 100ms are logged. The loop.slow_callback_duration attribute can be used to set the minimum execution duration in seconds that is considered “slow”.
"""


async def say_after(delay, msg):
    time.sleep(delay)  # blocking action
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
