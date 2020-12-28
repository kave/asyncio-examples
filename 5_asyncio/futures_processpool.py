from concurrent.futures import ProcessPoolExecutor
from time import sleep


def task(message):
    print('Sleeping...')
    sleep(2)
    print("Done Sleeping")
    return message


def main():
    executor = ProcessPoolExecutor(4)  # matches # of cores on your machine
    future = executor.submit(task, "Completed")
    print(f'Future isDone Status: {future.done()}')
    # sleep(3)
    # print(f'Future isDone Status: {future.done()}')
    # print(f'Future Result: {future.result()}')


if __name__ == '__main__':
    main()
