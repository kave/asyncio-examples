import gevent
import requests
import timeit


def fetch(pid):
    requests.get('http://google.com')  # blocking action on the interpreter
    print(f'Process {pid}')
    return ""


def synchronous():
    for i in range(1, 10):
        fetch(i)


def asynchronous():
    threads = []
    for i in range(1, 10):
        threads.append(gevent.spawn(fetch, i))  # bundles all of the threads (greenlets) in a queue
    gevent.joinall(threads)  # executes them them one at a time


print(f'Synchronous: {timeit.timeit(synchronous, number=1)}')
print(f'Asynchronous: {timeit.timeit(asynchronous, number=1)}')
