#!/usr/bin/env python

# WS server that sends messages every second

import asyncio
import datetime

import websockets


async def time(websocket, path):
    while True:
        await websocket.send(str(datetime.datetime.now()))
        await asyncio.sleep(1)


start_server = websockets.serve(time, '127.0.0.1', '9000')
print(f'Running server on 127.0.0.1:9000')

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
