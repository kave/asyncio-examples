#!/usr/bin/env python

# WS server example that synchronizes state across clients

import asyncio
import json
import logging

import websockets

logging.basicConfig()

COUNTER_STATE = {"value": 0}

USERS = set()


def counter_status():
    return json.dumps({"type": "state", **COUNTER_STATE})


def users_status():
    return json.dumps({"type": "users", "count": len(USERS)})


async def notify_counter_state():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = counter_status()
        await asyncio.wait([user.send(message) for user in USERS])


async def notify_users():
    if USERS:  # asyncio.wait doesn't accept an empty list
        message = users_status()
        await asyncio.wait([user.send(message) for user in USERS])


async def register(websocket):
    USERS.add(websocket)
    await notify_users()


async def unregister(websocket):
    USERS.remove(websocket)
    await notify_users()


async def counter(websocket, path):
    # register(websocket) sends user_event() to websocket
    await register(websocket)
    try:
        await websocket.send(counter_status())
        async for message in websocket:
            data = json.loads(message)
            if data["action"] == "minus":
                COUNTER_STATE["value"] -= 1
                await notify_counter_state()
            elif data["action"] == "plus":
                COUNTER_STATE["value"] += 1
                await notify_counter_state()
            else:
                logging.error("unsupported event: {}", data)
    finally:
        await unregister(websocket)


start_server = websockets.serve(counter, '127.0.0.1', '9000')
print(f'Running server on 127.0.0.1:9000')

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
