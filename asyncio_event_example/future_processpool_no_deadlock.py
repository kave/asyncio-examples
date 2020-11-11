from concurrent.futures import ProcessPoolExecutor
from time import sleep


def wait_on_b():
    sleep(2)
    print(f'B Result {b_future.result()}')  # b_future will never complete because it is waiting on a_future.
    return 5


def wait_on_a():
    sleep(2)
    print(f'A Result {a_future.result()}')  # a_future will never complete because it is waiting on b_future.
    return 6


# Will not deadlock since they are executed in separate processes, but will error due to undefined variables
if __name__ == '__main__':
    executor = ProcessPoolExecutor(max_workers=4)
    a_future = executor.submit(wait_on_b)
    b_future = executor.submit(wait_on_a)
    print(a_future)
    print(b_future)
    # sleep(3)
    # print(a_future.result())
    # print(b_future.result())
