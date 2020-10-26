import time
from threading import Thread, Condition


class StingySpendy:
    money = 100
    cv = Condition()

    def stingy(self):
        for i in range(1000000):
            self.cv.acquire()
            self.money += 10
            self.cv.notify()
            self.cv.release()
        print("Stingy Done")

    def spendy(self):
        for i in range(500000):
            self.cv.acquire()
            while self.money < 20:
                self.cv.wait()
            self.money -= 20
            if self.money < 0:
                print("Money in bank", self.money)
            self.cv.release()
        print("Spendy Done")


ss = StingySpendy()
Thread(target=ss.stingy, args=()).start()
Thread(target=ss.spendy, args=()).start()
time.sleep(5)
print("Money in the end", ss.money)
