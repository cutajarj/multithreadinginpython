from threading import Thread, Lock
import time


def red_robot(lock1, lock2):
    while True:
        print("Red: Acquiring lock1...")
        lock1.acquire()
        print("Red: Acquiring lock2...")
        lock2.acquire()
        print("Red: Locks Acquired")
        lock2.release()
        lock1.release()
        print("Red: Locks Released")
        time.sleep(0.5)


def blue_robot(lock1, lock2):
    while True:
        print("Blue: Acquiring lock2...")
        lock2.acquire()
        print("Blue: Acquiring lock1...")
        lock1.acquire()
        print("Blue: Locks Acquired")
        lock2.release()
        lock1.release()
        print("Blue: Locks Released")
        time.sleep(0.5)


mutex1 = Lock()
mutex2 = Lock()
red = Thread(target=red_robot, args=(mutex1, mutex2))
blue = Thread(target=blue_robot, args=(mutex1, mutex2))
red.start()
blue.start()


