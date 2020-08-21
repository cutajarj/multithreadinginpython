import time
from threading import Barrier, Thread

barrier = Barrier(2)


def wait_on_two_barriers(name, time_to_sleep):
    for i in range(10):
        print(name, "running")
        time.sleep(time_to_sleep)
        print(name, "is waiting on barrier")
        barrier.wait()
    print(name, "is finished")


red = Thread(target=wait_on_two_barriers, args=(["red", 4]))
blue = Thread(target=wait_on_two_barriers, args=(["blue", 10]))
red.start()
blue.start()
# time.sleep(8)
# print("Aborting barrier")
# barrier.abort()
# barrier.reset()
