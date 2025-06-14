from time import sleep
from threading import *

class hi(Thread):
    def run(self):
        for i in range(1500):
            print("hi")
            sleep(1)

class hello(Thread):
    def run(self):
        for i in range(1500):
            print("hello")
            sleep(1)

c1 = hi()
c1.start()
c2  = hello()
c2.start()
c1.join()
c2.join()
print("bye")