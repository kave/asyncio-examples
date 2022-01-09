import uvicorn


async def read_body(receive):
    """
    Read and return the entire body from an incoming ASGI message.
    """
    body = b''
    more_body = True

    while more_body:
        message = await receive()
        print(f"received msg {message.get('body', b'')}")
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
    print(f'Full request message: {body}')


if __name__ == "__main__":
    uvicorn.run("stream_eventloop:app", host='127.0.0.1', port='9000', log_level="info")
