from concurrent.futures import ThreadPoolExecutor
import time

a_future = None
b_future = None


def wait_on_b():
    time.sleep(2)  # blocking events
    print(b_future.result())  # b_future will never complete because it is waiting on a_future.
    return 5


def wait_on_a():
    time.sleep(2)
    print(a_future.result())  # a_future will never complete because it is waiting on b_future.
    return 6


# It will deadlock because they are sharing the same process, i.e sharing variables
if __name__ == '__main__':
    executor = ThreadPoolExecutor(max_workers=2)
    print(f"started at {time.strftime('%X')}")
    a_future = executor.submit(wait_on_b)  # return 5
    b_future = executor.submit(wait_on_a)  # return 6
    print(a_future)
    print(b_future)

    # time.sleep(2)
    #
    # print(a_future.result())
    # print(b_future.result())
    print(f"finished at {time.strftime('%X')}")
