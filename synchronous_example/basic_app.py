from flask import Flask, request

import config

app = Flask(__name__)


@app.route('/')
def hello_world():
    print(request)
    print(request.headers)
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT)
