import time
from threading import Thread, Lock


class StingySpendy:
    money = 100
    mutex = Lock()

    def stingy(self):
        for i in range(1000000):
            self.mutex.acquire()
            self.money += 10
            self.mutex.release()
        print("Stingy Done")

    def spendy(self):
        for i in range(1000000):
            self.mutex.acquire()
            self.money -= 10
            self.mutex.release()
        print("Spendy Done")


ss = StingySpendy()
st = Thread(target=ss.stingy, args=())
sp = Thread(target=ss.spendy, args=())
st.start()
sp.start()
time.sleep(5)
print("Money in the end", ss.money)
