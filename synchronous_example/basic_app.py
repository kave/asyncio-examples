from flask import Flask

import config

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host=config.HOST, port=config.PORT)
