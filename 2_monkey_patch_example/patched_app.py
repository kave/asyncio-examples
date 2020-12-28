import gevent.monkey

gevent.monkey.patch_socket()  # http://www.gevent.org/intro.html
"""
The gevent.socket.gethostbyname() function has the same interface as the 
standard socket.gethostbyname() but it does not block the whole interpreter 
and thus lets the other greenlets proceed with their requests unhindered.
"""
import gevent
import requests
import timeit


def make_request(pid):
    requests.get('http://google.com')  # blocks the whole interpreter and results in serialized behavior
    print(f'Process {pid}')
    return ""


def synchronous():
    for i in range(1, 10):
        make_request(i)


def asynchronous():
    threads = []
    for i in range(1, 10):
        threads.append(gevent.spawn(make_request, i))  # bundles all of the threads(greenlets) in a queue
    gevent.joinall(threads)  # executes them concurrently


print(f'Synchronous: {timeit.timeit(synchronous, number=1)}\n')
print(f'Asynchronous: {timeit.timeit(asynchronous, number=1)}')
