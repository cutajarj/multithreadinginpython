import time
from threading import Thread


def do_work():
    print("Starting work")
    time.sleep(1)
    print("Finished work")


for _ in range(5):
    t = Thread(target=do_work, args=())
    t.start()

