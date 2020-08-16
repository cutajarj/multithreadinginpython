import time
from threading import Thread


def child():
    print("Child Thread doing work...")
    time.sleep(5)
    print("Child Thread Done...")


def parent():
    t = Thread(target=child, args=([]))
    t.start()
    print("Parent Thread is waiting...")
    t.join()
    print("Parent Thread is unblocked...")


parent()
