import time

import requests


def generate_request():
    print('Sending 1st Msg')
    yield b'hi'
    print('Sleeping.....')
    time.sleep(5)
    print('Sending 2nd Msg')
    yield b'there'


with requests.Session() as client:
    resp = client.post(f'http://127.0.0.1:9000', data=generate_request())
    print(resp, resp.text.strip())
