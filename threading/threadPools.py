# Import necessary libraries
import time
from concurrent.futures import ThreadPoolExecutor

# Function to check if a number is odd or even
def worker(number):
    # Simulate a task taking 2 seconds to complete
    time.sleep(2)
    
    # Check if the number is even or odd
    if number % 2 == 0:
        print(f"The number {number} is even.")
        return f"{number}: Even"
    else:
        print(f"The number {number} is odd.")
        return f"{number}: Odd"

# Driver code

# Create a ThreadPoolExecutor with a maximum of 2 worker threads
pool = ThreadPoolExecutor(2)

# Submit tasks to the thread pool
work = pool.submit(worker, 42)  # Submit a task for the number 42
work2 = pool.submit(worker, 55)  # Submit a task for the number 55
work3 = pool.submit(worker, 2)  # Submit a task for the number 2
work4 = pool.submit(worker, 3)  # Submit a task for the number 3

# Get the result of a specific task (work2 in this case)
print(work2.result())

# Shut down the thread pool so that it does not accept any new tasks
pool.shutdown()

# Try submitting a new task after shutting down the pool
try:
    # This will raise an exception as the pool has been shutdown
    workX = pool.submit(worker, 32)
except:
    print("Raising exception error. Cannot take new submission as the pool has been shutdown")
