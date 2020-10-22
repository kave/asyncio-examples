import uvicorn

import config


async def read_body(receive):
    """
    Read and return the entire body from an incoming ASGI message.
    """
    body = b''
    more_body = True

    while more_body:
        message = await receive()
        body += message.get('body', b'') + b' '
        more_body = message.get('more_body', False)  # checks if the request is done sending messages

    return body


async def app(scope, receive, send):
    assert scope['type'] == 'http'

    body = await read_body(receive)

    await send({
        'type': 'http.response.start',
        'status': 200,
        'headers': [
            [b'content-type', b'text/plain'],
        ],
    })

    await send({
        'type': 'http.response.body',
        'body': body,
    })
    print(body)


if __name__ == "__main__":
    uvicorn.run("stream_eventloop:app", host=config.HOST, port=config.PORT, log_level="info")
