import multiprocessing
import time
from multiprocessing.context import Process


def do_work():
    print("Starting work")
    time.sleep(1)
    print("Finished work")


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    for _ in range(5):
        p = Process(target=do_work, args=())
        p.start()

