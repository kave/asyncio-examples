from concurrent.futures import ThreadPoolExecutor
from time import sleep


def wait_on_b():
    sleep(2)
    print(b.result())  # b will never complete because it is waiting on a.
    return 5


def wait_on_a():
    sleep(2)
    print(a.result())  # a will never complete because it is waiting on b.
    return 6


# It will deadlock because they are sharing the same process
if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=2)
    a = executor.submit(wait_on_b)
    b = executor.submit(wait_on_a)
    print(a)
    print(b)
    # sleep(3)
    # print(a.result())
    # print(b.result())
