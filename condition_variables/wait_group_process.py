from multiprocessing import Condition, Value, Process

import time


# note this is the equivalent of a waitgroup for a process instead of a thread
class WaitGroupProcess:
    def __init__(self, cv, wait_count):
        self.cv = cv
        self.wait_count = wait_count

    def add(self, count):
        self.cv.acquire()
        self.wait_count.value += count
        self.cv.release()

    def done(self):
        self.cv.acquire()
        if self.wait_count.value > 0:
            self.wait_count.value -= 1
        if self.wait_count.value == 0:
            self.cv.notify_all()
        self.cv.release()

    def wait(self):
        self.cv.acquire()
        while self.wait_count.value > 0:
            self.cv.wait()
        self.cv.release()


def sleep_and_done(condC, wc, time_to_sleep):
    wg = WaitGroupProcess(condC, wc)
    time.sleep(time_to_sleep)
    wg.done()
    print("Process called done")


if __name__ == '__main__':
    wait_count = Value('i', 0, lock=False)
    cv = Condition()
    wait_group_process = WaitGroupProcess(cv, wait_count)
    wait_group_process.add(3)
    Process(target=sleep_and_done, args=(cv, wait_count, 2)).start()
    Process(target=sleep_and_done, args=(cv, wait_count, 5)).start()
    Process(target=sleep_and_done, args=(cv, wait_count, 7)).start()
    wait_group_process.wait()
    print("All processes complete")
