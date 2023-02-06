import time
import threading 

def worker(name):
    time.sleep(1)
    print(f"{name} Completed! Yay")


threadOne = threading.Thread(target=worker("Thread two"))
threadTwo =threading.Thread(target=worker("Thread one"))

threadTwo.start()
threadOne.start()