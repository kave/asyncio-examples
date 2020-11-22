#!/usr/bin/env python

# WS server that sends messages at random intervals

import asyncio
import datetime
import random

import websockets

import config


async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)


start_server = websockets.serve(time, config.HOST, config.PORT)
print(f'Running server on {config.HOST}:{config.PORT}')

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
