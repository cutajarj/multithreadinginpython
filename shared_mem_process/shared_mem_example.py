import multiprocessing
from multiprocessing.context import Process

import time


def print_array_contents(array):
    while True:
        for i in range(len(array)):
            print(array[i])
        time.sleep(1)


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
#    arr = [1] * 10
    arr = multiprocessing.Array('i', [-1] * 10) # lock=true
    p = Process(target=print_array_contents, args=([arr]))
    p.start()
    for j in range(10):
        time.sleep(2)
        for i in range(10):
            arr[i] = j
