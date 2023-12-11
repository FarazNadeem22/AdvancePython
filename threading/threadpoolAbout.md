## Explanation of the Program

The given Python script demonstrates the use of ThreadPoolExecutor from the concurrent.futures module to execute tasks concurrently using multiple worker threads. Here's a breakdown of the program's functionality:

### Importing Necessary Libraries:

The script imports required libraries:
- `time`: Used for time-related functions.
- `ThreadPoolExecutor` from `concurrent.futures`: Provides a thread pool for concurrent execution of tasks.

### Function Definition (`worker`):

- **Task Simulation**: The `worker` function simulates a task taking 2 seconds to complete using `time.sleep(2)`.
- **Odd-Even Check**: It checks if a given number is odd or even and prints a corresponding message.
- **Return Value**: The function returns a string indicating whether the number is odd or even.

### Driver Code:

- **ThreadPoolExecutor Creation**: Creates a ThreadPoolExecutor with a maximum of 2 worker threads (`pool = ThreadPoolExecutor(2)`).
- **Task Submission**: Submits four tasks (`work`, `work2`, `work3`, `work4`) to the thread pool using `pool.submit()`, passing different numbers to the `worker` function.
- **Task Execution and Result Retrieval**: Executes tasks asynchronously and immediately prints the result of a specific task (`work2.result()`).

### ThreadPool Shutdown:

- **Shutdown Pool**: Invokes `pool.shutdown()` to stop the thread pool from accepting any new tasks. It waits for the active tasks to complete but doesn't accept new submissions.

### Exception Handling:

- **Submitting Task After Pool Shutdown**: Attempts to submit a new task (`workX = pool.submit(worker, 32)`) after shutting down the pool.
- **Exception Handling**: Catches the exception raised due to attempting to submit a task to a closed pool and prints an error message accordingly.

The program showcases concurrent execution of tasks using a ThreadPoolExecutor, task submission, result retrieval, pool shutdown, and proper exception handling for task submission after the pool has been shut down.
