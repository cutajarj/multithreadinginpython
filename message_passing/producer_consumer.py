from queue import Queue
from threading import Thread

import time


def consumer(q):
    while (True):
        txt = q.get()
        print(txt)
        time.sleep(1)


def producer(q):
    while (True):
        q.put("Hello there")
        print("Message Sent")


q = Queue(maxsize=10)
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()
