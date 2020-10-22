from concurrent.futures import ProcessPoolExecutor
from time import sleep


def task(message):
    sleep(2)
    print("done")
    return message


def main():
    executor = ProcessPoolExecutor(5)
    future = executor.submit(task, "Completed")
    print(future.done())
    # sleep(3)
    # print(future.done())
    # print(future.result())


if __name__ == '__main__':
    main()
