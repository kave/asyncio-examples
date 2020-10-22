from time import sleep

from flask import Flask

import config

app = Flask(__name__)


@app.route('/')
def hello_world():
    print("does some processing")
    sleep(5)
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT)
