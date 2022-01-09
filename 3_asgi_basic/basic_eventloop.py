import pprint

import uvicorn


async def app(scope, receive, send):
    assert scope['type'] == 'http'
    pprint.pprint(scope)

    # sends the response in chunks
    # 1) alerts the client that the response will begin transferring
    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })

    # 2) transmits the response body
    await send({
        'type': 'http.response.body',
        'body': b'Hello, world!',
    })


if __name__ == "__main__":
    uvicorn.run("basic_eventloop:app", host='127.0.0.1', port='9000', log_level="info")
