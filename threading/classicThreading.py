import time
import threading 

# Function to simulate a task
def worker(name):
    time.sleep(1)  # Simulate task delay of 1 second
    print(f"{name} Completed! Yay")  # Print completion message with the provided name

# Create two threads for concurrent execution

# Incorrect usage: Invoking worker function immediately and assigning the result to the target of threadOne
# As a result, worker function is executed in the main thread rather than in a separate thread
threadOne = threading.Thread(target=worker("Thread two"))

# Incorrect usage: Invoking worker function immediately and assigning the result to the target of threadTwo
# As a result, worker function is executed in the main thread rather than in a separate thread
threadTwo = threading.Thread(target=worker("Thread one"))

# Start the threads for concurrent execution

# Start the threadTwo (Incorrectly created)
threadTwo.start()

# Start the threadOne (Incorrectly created)
threadOne.start()
