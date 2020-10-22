from concurrent.futures import ProcessPoolExecutor
from time import sleep


def wait_on_b():
    sleep(2)
    print(f'B Result {b.result()}')  # b will never complete because it is waiting on a.
    return 5


def wait_on_a():
    sleep(2)
    print(f'A Result {a.result()}')  # a will never complete because it is waiting on b.
    return 6


# Will not deadlock since they are executed in separate processes, but will error due to undefined variables
if __name__ == '__main__':
    executor = ProcessPoolExecutor(max_workers=4)
    a = executor.submit(wait_on_b)
    b = executor.submit(wait_on_a)
    print(a)
    print(b)
    # sleep(3)
    # print(a.result())
    # print(b.result())
