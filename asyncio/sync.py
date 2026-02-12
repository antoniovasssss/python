import time # imported time module, provides time-related functions

def task(name): # defines function called task that takes one parameter called name
    print(f"Starting task {name}") # prints message showing which task is starting 
    time.sleep(2) # execution is paused for 2 seconds, simulating a task that takes time to complete
    print(f"Finished task {name}") # prints a message showing that the task has completed

start_time = time.time() # records the current time (in seconds) before the task begin

task("A") # calls the task function three times sequentially with names "A", "B", and "C". Each call will take about 2 seconds, running one after another
task("B")
task("C")

end_time = time.time() # records the current time all the tasks have finished

print("Total time:", end_time - start_time) # calculates and prints the total elapsed time by subtractinng the start time from the end time