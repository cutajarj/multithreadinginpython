from threading import Thread, Lock
import time


def red_robot(lock1, lock2):
    while True:
        print("Red: Acquiring lock 1...")
        lock1.acquire()
        print("Red: Acquiring lock 2...")
        lock2.acquire()
        print("Red: Locks acquired...")
        lock1.release()
        lock2.release()
        print("Red: Locks released")
        time.sleep(0.5)

def blue_robot(lock1, lock2):
    while True:
        print("Blue: Acquiring lock 2...")
        lock2.acquire()
        print("Blue: Acquiring lock 1...")
        lock1.acquire()
        print("Blue: Locks acquired...")
        lock1.release()
        lock2.release()
        print("Blue: Locks released")
        time.sleep(0.5)


mutex1 = Lock()
mutex2 = Lock()
red = Thread(target=red_robot, args=(mutex1, mutex2))
blue = Thread(target=blue_robot, args=(mutex1, mutex2))
red.start()
blue.start()



