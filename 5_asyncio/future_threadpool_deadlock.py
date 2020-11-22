from concurrent.futures import ThreadPoolExecutor
from time import sleep


def wait_on_b():
    sleep(2)
    print(b_future.result())  # b_future will never complete because it is waiting on a_future.
    return 5


def wait_on_a():
    sleep(2)
    print(a_future.result())  # a_future will never complete because it is waiting on b_future.
    return 6


# It will deadlock because they are sharing the same process, i.e sharing variables
if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=2)
    a_future = executor.submit(wait_on_b)
    b_future = executor.submit(wait_on_a)
    print(a_future)
    print(b_future)
    # sleep(3)
    # print(a_future.result())
    # print(b_future.result())
