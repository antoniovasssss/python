import asyncio # imports pythons asyncio module for asyncronous programming
import time # imports the time module

async def task(name): # defines an (async)ronous function called task. The async keyword marks it as a coroutine that can be paused and resumed
    print(f"Starting task {name}") # prints which task is starting
    await asyncio.sleep(2) # pauses this specific task for 2 seconds without blocking other tasks. The await keyword allows other tasks to run during this wait time
    print(f"Finished task {name}") # prints when the task completes 
    return f"Result of task {name}" # returns a string result from the task 

async def run_asyncio(): # defines another asyncronous function to coordinate running multiple tasks
    results = await asyncio.gather(task("A"), task("B"), task("C")) # runs all three tasks concurrently (at the same time). It waits for all of them to complete and collects their return values in order
    return list(results) # converts and returns the results as a list

if __name__ == "__main__": # ensures the following code only runs when the script is executed directly (not imported)
    start_time = time.perf_counter() # records the start time using perf_counter() which is more precise than time.time() for measuring performance
    results = asyncio.run(run_asyncio()) # starts the asyncio event loop and runs the run_asyncio() function. This is the entry point for async code
    elapsed_time = time.perf_counter() - start_time # calculates total elapsed time

    print("Asyncio results") # prints each tasks result
    for result in results:
        print(f"{result}")

    print(f"\nTotal time: {elapsed_time:.2f} seconds") # prints the total time formatted to 2 decimal places
    print("Note: Tasks ran concurrently using asyncio - modern approach for I/O-bound tasks") # prints an explanatory note