import time

import requests

import config

s = requests.Session()


def generate_response():
    yield b'hi'
    time.sleep(5)
    yield b'there'


with requests.Session() as client:
    print(client.post(f'http://{config.HOST}:{config.PORT}', data=generate_response()))
