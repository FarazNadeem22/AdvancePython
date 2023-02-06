import time
from concurrent.futures import ThreadPoolExecutor

def worker(number):
    time.sleep(2)
    if number % 2 == 0:
        print(f"The number {number} is even.")
        return f"{number}: Even"
    else:
        print(f"The number {number} is odd.")
        return f"{number}: Odd"



""" Driver"""
# The argument is the number of tasks in case of two it will run in batches of two.
pool = ThreadPoolExecutor(2)
work = pool.submit(worker,42)
work2 = pool.submit(worker,55)
work3 = pool.submit(worker,2)
work4 = pool.submit(worker,3)

print(work2.result())

# Shutting down the pool 
pool.shutdown()

try:
    workX = pool.submit(worker,32)
except:
    print("Raising exception error. Cannot take new submission as the pool has been shutdown")