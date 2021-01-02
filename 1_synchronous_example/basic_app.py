from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    print(request)
    print(request.headers)
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='9000', threaded=True)
