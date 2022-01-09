from time import sleep

from flask import Flask

app = Flask(__name__)

"""
The Python Global Interpreter Lock or GIL, in simple words, is a mutex (or a lock) 
that allows only one thread to hold the control of the Python interpreter. 
This means that only one thread can be in a state of execution at any point in time.
"""


@app.route('/')
def hello_world():
    print("does some processing")
    sleep(10)  # blocks the python interpreter
    return 'Hello, World!'


@app.route('/healthz')
def healthz():
    return 'OK'


if __name__ == '__main__':
    app.run(host='127.0.0.1', port='9000', threaded=False)
